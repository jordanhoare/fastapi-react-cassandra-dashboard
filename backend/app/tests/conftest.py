from typing import Generator

import pytest
from fastapi.testclient import TestClient

from app.application import app


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as test_client:
        yield test_client
