import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT


from database.base import Base


class Mc5Aeid(Base):
    """Maps to mc5_aeid table in invitrodb databases."""

    __tablename__ = 'mc5_aeid'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    aeid = Column(BIGINT, nullable=False, primary_key=True)
    mc5_mthd_id = Column(Integer, nullable=False, primary_key=True)

    modified_by = Column(String(100))
    created_date = Column(DateTime, default=datetime.datetime.now, nullable=False)
    modified_date = Column(DateTime, default=datetime.datetime.now, nullable=False)