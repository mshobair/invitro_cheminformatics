import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT


from database.base import Base


class Mc5Chid(Base):
    """Maps to mc5_chid table in invitrodb databases."""

    __tablename__ = 'mc5_chid'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    m5id = Column(BIGINT, nullable=False, primary_key=True)
    chid_rep = Column(TINYINT, nullable=False)
