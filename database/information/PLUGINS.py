import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT, LONGTEXT

from database.base import Base


class Plugins(Base):
    """Maps to PLUGINS table in information databases."""

    __tablename__ = 'PLUGINS'
    __table_args__ = {'schema': Schemas.information_schema}

    PLUGIN_NAME = Column(String, nullable=False)
    PLUGIN_VERSION = Column(String, nullable=False)
    PLUGIN_STATUS = Column(String, nullable=False)
    PLUGIN_TYPE = Column(String, nullable=False)
    PLUGIN_TYPE_VERSION = Column(String, nullable=False)
    PLUGIN_LIBRARY = Column(String)
    PLUGIN_LIBRARY_VERSION = Column(String)
    PLUGIN_AUTHOR = Column(String)
    PLUGIN_DESCRIPTION = Column(LONGTEXT)
    PLUGIN_LICENSE = Column(String)
    LOAD_OPTION = Column(String, nullable=False)