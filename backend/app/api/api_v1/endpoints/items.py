import logging
import uuid
from typing import Any, List

import pandas as pd
from cassandra.concurrent import execute_concurrent_with_args
from cassandra.cqlengine import connection, query
from fastapi import APIRouter, Depends, FastAPI, HTTPException

from app.api.deps import get_session
from app.api.utils import DataGenerator, unix_time, unix_time_millis
from app.schemas import DashboardItems, Rentals

router = APIRouter()


@router.get("", response_model=DashboardItems)
async def dashboard(session=Depends(get_session)) -> Any:
    """Select dashboard items and serve them front pydantic"""

    logger = logging.getLogger("uvicorn.access")

    try:
        result = session.execute(
            f"SELECT * FROM cql_keyspace.rentals WHERE car_make = 'Toyota' and car_model = 'Camry'"
        )
        df = pd.DataFrame(list(result))
        return DashboardItems(recent_returns=df.to_dict(orient="records"))
    except Exception as e:
        raise HTTPException(status_code=404, detail=e)
        logger.error(e)


@router.post("")
async def generate_dummy_data(records: int, session=Depends(get_session)) -> List:
    """
    Provide an integer to generate a random set of car propeties.
    Number plates are stored in a dict and validated before comipling a list to ensure
    duplicate registration plates aren't out at the same time
    """

    logger = logging.getLogger("uvicorn.access")

    # Create a keyspace
    session.execute(
        """
    CREATE KEYSPACE IF NOT EXISTS cql_keyspace
    WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': 1 } 
    AND durable_writes = 'true';
    """
    )

    # Create our table
    session.execute(
        """
    CREATE TABLE IF NOT EXISTS cql_keyspace.rentals (
    car_make text,
    car_model text,
    rental_start_time timestamp,
    rental_end_time timestamp,
    car_category text,
    car_year int,
    registration_number text,
    driver_license text,
    first_name text,
    last_name text,
    contact_number text,
    PRIMARY KEY ((car_make, car_model), rental_start_time, rental_end_time)
    ) WITH default_time_to_live = 2592000;
    """
    )

    statement = session.prepare(
        """
                                INSERT INTO cql_keyspace.rentals (car_make,
                                car_model,
                                rental_start_time,
                                rental_end_time,
                                car_category,
                                car_year,
                                registration_number,
                                driver_license,
                                first_name,
                                last_name,
                                contact_number) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                                """
    )

    try:
        # Prepare data. execute concurrently with statement, parameters, args
        records = DataGenerator().generate_records(num_records=records)
        parameters = [x for x in records]
        execute_concurrent_with_args(session, statement, parameters, concurrency=50)
        return list(session.execute("SELECT * FROM cql_keyspace.rentals"))

    except Exception as e:
        raise HTTPException(status_code=404, detail=e)
        logger.error(e)


@router.delete("")
async def delete_rentals_table(session=Depends(get_session)) -> Any:
    """Select dashboard items and serve them front pydantic"""
    session.execute("DROP TABLE IF EXISTS cql_keyspace.rentals;")
    try:
        results = session.execute("SELECT * FROM cql_keyspace.rentals;")
        return list(result)
    except Exception:
        pass
