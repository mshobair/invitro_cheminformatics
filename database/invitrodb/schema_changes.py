import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT


from database.base import Base


class SchemaChanges(Base):
    """Maps to schema_changes table in invitrodb databases."""

    __tablename__ = 'schema_changes'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    id = Column(Integer, nullable=False, primary_key=True)
    filename = Column(String(255), nullable=False)
    short_description = Column(String(255), nullable=False)

    created_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)
