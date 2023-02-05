import datetime
from typing import Optional

from pydantic import BaseModel


class Rentals(BaseModel):
    car_make: Optional[str] = None
    car_model: Optional[str] = None
    rental_start_time: Optional[datetime.datetime] = None
    rental_end_time: Optional[datetime.datetime] = None
    car_category: Optional[str] = None
    car_year: Optional[int] = None
    contact_number: Optional[str] = None
    driver_license: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    registration_number: Optional[str] = None
