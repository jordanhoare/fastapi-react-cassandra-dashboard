from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Class model for local environment variables."""

    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 8000
    SERVER_DEBUG_MODE: bool = False
    SERVER_WORKERS: int = 1
    API_V1_STR: str = "/api/v1"
    CASSANDRA_HOST: str = "cassandra"
    CASSANDRA_PORT: int = 9042
    CASSANDRA_USER: str = "cassandra"
    CASSANDRA_PWD: str = "cassandra"
    CASSANDRA_KEYSPACE: str = "main_keyspace"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> Settings:
    return Settings()
