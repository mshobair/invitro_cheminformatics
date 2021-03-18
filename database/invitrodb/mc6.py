import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT


from database.base import Base


class Mc6(Base):
    """Maps to mc6 table in invitrodb databases."""

    __tablename__ = 'mc6'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    m6id = Column(BIGINT, nullable=False, primary_key=True)
    m5id = Column(BIGINT, nullable=False)
    m4id = Column(BIGINT, nullable=False)
    aeid = Column(BIGINT, nullable=False)
    mc6_mthd_id = Column(BIGINT, nullable=False)
    flag = Column(String(255), nullable=False)
    fval = Column(DOUBLE)
    fval_unit = Column(String(45))

    modified_by = Column(String(100))
    created_date = Column(DateTime, default=datetime.datetime.now, nullable=False)
    modified_date = Column(DateTime, default=datetime.datetime.now, nullable=False)