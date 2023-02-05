from app.db import create_session


def get_session():
    """Yields a database session."""
    session = create_session()
    try:
        yield session
    finally:
        pass
