import datetime
from typing import List

from pydantic import BaseModel

from app.schemas.rentals import Rentals


class DashboardItems(BaseModel):
    recent_returns: List[Rentals]
