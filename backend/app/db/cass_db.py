import logging

from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster

from app.core.config import get_settings


def create_session():
    logger = logging.getLogger("uvicorn.access")
    settings = get_settings()
    auth = PlainTextAuthProvider(username=settings.CASSANDRA_USER, password=settings.CASSANDRA_PWD)
    cluster = Cluster(
        contact_points=[settings.CASSANDRA_HOST], port=settings.CASSANDRA_PORT, auth_provider=auth
    )
    try:
        session = cluster.connect()

        session.execute(
            """
        CREATE KEYSPACE IF NOT EXISTS main_keyspace
        WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': 1 }
        AND durable_writes = 'true';
        """
        )

        session.set_keyspace(settings.CASSANDRA_KEYSPACE)

        return session

    except Exception as e:
        logger.error("Cassandra connection error. Attempt reconnection")
        logger.error(e)
