import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class MentorPostdocs(Base):
    """Maps to mentor_postdocs table in chemprop databases."""

    __tablename__ = 'mentor_postdocs'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    post_doc_id = Column(Integer)
    pi_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)