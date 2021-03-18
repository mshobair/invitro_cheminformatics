import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class AgreementStatuses(Base):
    """Maps to agreement_statuses table in chemprop databases."""

    __tablename__ = 'agreement_statuses'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    status = Column(String)