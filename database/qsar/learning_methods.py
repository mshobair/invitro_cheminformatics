import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class LearningMethods(Base):
    """Maps to learning_methods table in qsar databases."""

    __tablename__ = 'learning_methods'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    method_name = Column(String(255))
    method_description = Column(String(255))
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)