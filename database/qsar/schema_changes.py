import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class SchemaChanges(Base):
    """Maps to schema_changes table in qsar databases."""

    __tablename__ = 'schema_changes'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    filename = Column(String, nullable=False)
    short_description = Column(String, nullable=False)
    created_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
