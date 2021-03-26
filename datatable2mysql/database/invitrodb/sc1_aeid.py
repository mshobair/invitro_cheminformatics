import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT


from database.base import Base


class Sc1Aeid(Base):
    """Maps to sc1_aeid table in invitrodb databases."""

    __tablename__ = 'sc1_aeid'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    sc1_mthd_id = Column(Integer, nullable=False, primary_key=True)
    aeid = Column(Integer, nullable=False, primary_key=True)
    exec_ordr = Column(Integer, nullable=False)

    modified_by = Column(String(100), nullable=False)
    created_date = Column(DateTime, default=datetime.datetime.now, nullable=False)
    modified_date = Column(DateTime, default=datetime.datetime.now, nullable=False)