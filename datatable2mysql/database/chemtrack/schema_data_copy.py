import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class SchemaDataCopy(Base):
    """Maps to schema_data_copy table in chemprop databases."""

    __tablename__ = 'schema_data_copy'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    filename_yaml = Column(String, nullable=False)
    dbms_src = Column(String, nullable=False)
    dbms_dst = Column(String, nullable=False)
    db_src = Column(String, nullable=False)
    db_dst = Column(String, nullable=False)
    number_of_tables_src = Column(Integer, nullable=False)
    number_of_tables_dst = Column(Integer, nullable=False)
    success = Column(Integer)
    created_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
