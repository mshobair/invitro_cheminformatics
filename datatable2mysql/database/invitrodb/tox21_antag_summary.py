import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT


from database.base import Base


class Tox21AntagSummary(Base):
    """Maps to tox21_antag_summary table in invitrodb databases."""

    __tablename__ = 'tox21_antag_summary'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    Assay_Name = Column(String)
    Protocol_Name = Column(String)
    Name_of_control_compound = Column(String)
    Concentration_used_in_antagonist_mode = Column(String)
    Hill_Coef = Column(String)
    Calculating_ECXX = Column(String)
    Online_Validation_EC50 = Column(String)
    Online_Screening_EC50 = Column(String)
    Validation_sample_size = Column(String)
    Screening_sample_size = Column(String)
    aid = Column(BIGINT)
    Antag_assay_name = Column(String)


