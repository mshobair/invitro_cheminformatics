import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime

from database.base import Base


class Users(Base):
    """Maps to users table in chemprop databases."""

    __tablename__ = 'users'
    __table_args__ = {'schema': Schemas.qsar_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    encrypted_password = Column(String, nullable=False)
    reset_password_token = Column(String)
    remember_created_at = Column(DateTime)
    sing_in_count = Column(Integer, nullable=False, default=0)
    current_sign_in_at = Column(DateTime)
    last_sign_in_at = Column(DateTime)
    current_sign_in_ip = Column(String)
    last_sign_in_ip = Column(String)
    f_name = Column(String)
    l_name = Column(String)
    picture = Column(String)
    role_id = Column(Integer)
    username = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)