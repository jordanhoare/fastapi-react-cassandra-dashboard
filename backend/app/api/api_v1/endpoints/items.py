import uuid

from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def root():

    # from app.db import create_session

    # session = create_session()
    # # Create a keyspace
    # session.execute(
    #     """
    # CREATE KEYSPACE IF NOT EXISTS cql_keyspace
    # WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': 1 }
    # AND durable_writes = 'true';
    # """
    # )
    # # Create tables in cql_keyspace for car makes
    # session.execute(
    #     "CREATE TABLE IF NOT EXISTS cql_keyspace.cars_by_id (id int PRIMARY KEY, make text, model text)"
    # )
    # # Insert a record into each keyspace table
    # session.execute(
    #     "INSERT INTO cql_keyspace.cars_by_id (id, make, model) VALUES (1, 'Toyota', 'Camry')"
    # )
    # # Execute a CQL query to retrieve the record from the cars_by_id table
    # result = session.execute("SELECT * FROM cql_keyspace.cars_by_id WHERE id = 1")
    # return list(result)

    return {
        "recent_returns": [
            {
                "registration_number": 1,
                "car_make": "Camera Lens",
                "car_model": "Camera Lens",
                "car_category": "Camera Lens",
                "rental_start_time": 2,
                "rental_end_time": 40570,
            },
            {
                "registration_number": 2,
                "car_make": 69,
                "car_model": "Camera Lens",
                "car_category": "Camera Lens",
                "rental_start_time": 2,
                "rental_end_time": 40570,
            },
        ]
    }
