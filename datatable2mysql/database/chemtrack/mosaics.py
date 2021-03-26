import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class Mosaics(Base):
    """Maps to mosaics table in chemprop databases."""

    __tablename__ = 'mosaics'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    filename = Column(String)
    file_url = Column(String)
    file_kilobytes = Column(Integer)
    file_record_count = Column(Integer)
    added_by_user_id = Column(Integer)
    user_id = Column(Integer)
    file_app_name = Column(String)
    inserts = Column(Integer)
    deletes = Column(Integer)
    updates = Column(Integer)
    processing = Column(Integer, default=1)
    is_valid = Column(Integer)
    bottle_count = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)