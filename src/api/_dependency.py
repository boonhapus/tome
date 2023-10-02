import os

from sqlalchemy.engine import Connection
import sqlalchemy as sa


def get_database_connection() -> Connection:
    """Yield a Database connection."""
    engine = sa.create_engine(os.environ["DATABASE_JDBC_URL"])

    with engine.begin() as transaction:
        yield transaction
