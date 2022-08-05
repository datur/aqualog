from sqlalchemy import create_engine
from server.config import get_postgres_uri
from sqlalchemy.orm import sessionmaker

session_factory = sessionmaker(
    bind=create_engine(
        get_postgres_uri(),
        isolation_level="SERIALIZABLE",
    )
)