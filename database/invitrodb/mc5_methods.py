import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT


from database.base import Base


class Mc5Methods(Base):
    """Maps to mc5_methods table in invitrodb databases."""

    __tablename__ = 'mc5_methods'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    mc5_mthd_id = Column(Integer, nullable=False, primary_key=True)
    mc5_mthd = Column(String(50), nullable=False)
    desc = Column(String(255))

    modified_by = Column(String(100))
    created_date = Column(DateTime, default=datetime.datetime.now, nullable=False)
    modified_date = Column(DateTime, default=datetime.datetime.now, nullable=False)