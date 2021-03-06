import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP


from database.base import Base


class Mc2(Base):
    """Maps to mc2 table in invitrodb databases."""

    __tablename__ = 'mc2'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    m2id = Column(BIGINT, nullable=False, primary_key=True)
    m0id = Column(BIGINT)
    acid = Column(BIGINT)
    m1id = Column(BIGINT)
    cval = Column(DOUBLE, nullable=False)
    modified_by = Column(String(100))
    created_date = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_date = Column(DateTime, default=datetime.datetime.now, nullable=False)