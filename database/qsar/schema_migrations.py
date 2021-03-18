import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class SchemaMigrations(Base):
    """Maps to schema_migrations table in qsar databases."""

    __tablename__ = 'schema_migrations'
    __table_args__ = {'schema': Schemas.qsar_schema}

    version = Column(String, nullable=False, primary_key=True)