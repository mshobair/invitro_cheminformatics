import datetime

from database.database_schemas import Schemas
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.mysql import BIGINT, SMALLINT, DOUBLE, TIMESTAMP, TINYINT


from database.base import Base


class Mc4(Base):
    """Maps to mc4 table in invitrodb databases."""

    __tablename__ = 'mc4'
    __table_args__ = {'schema': Schemas.invitrodb_schema}

    m4id = Column(BIGINT, nullable=False, primary_key=True)
    aeid = Column(BIGINT, nullable=False)
    spid = Column(String(50), nullable=False)
    bmad = Column(DOUBLE, nullable=False)
    resp_max = Column(DOUBLE, nullable=False)
    resp_min = Column(DOUBLE, nullable=False)
    max_mean = Column(DOUBLE, nullable=False)
    max_mean_conc = Column(DOUBLE, nullable=False)
    max_med = Column(DOUBLE, nullable=False)
    max_med_conc = Column(DOUBLE, nullable=False)
    logc_max = Column(DOUBLE, nullable=False)
    logc_min = Column(DOUBLE, nullable=False)
    cnst = Column(TINYINT)
    hill = Column(TINYINT)
    hcov = Column(TINYINT)
    gnls = Column(TINYINT)
    gcov = Column(TINYINT)
    cnst_er = Column(DOUBLE)
    cnst_aic = Column(DOUBLE)
    cnst_rmse = Column(DOUBLE)
    cnst_prob = Column(DOUBLE)
    hill_tp = Column(DOUBLE)
    hill_tp_sd = Column(DOUBLE)
    hill_ga = Column(DOUBLE)
    hill_ga_sd = Column(DOUBLE)
    hill_gw = Column(DOUBLE)
    hill_gw_sd = Column(DOUBLE)
    hill_er = Column(DOUBLE)
    hill_er_sd = Column(DOUBLE)
    hill_aic = Column(DOUBLE)
    hill_rmse = Column(DOUBLE)
    hill_prob = Column(DOUBLE)
    gnls_tp = Column(DOUBLE)
    gnls_tp_sd = Column(DOUBLE)
    gnls_ga = Column(DOUBLE)
    gnls_ga_sd = Column(DOUBLE)
    gnls_gw = Column(DOUBLE)
    gnls_gw_sd = Column(DOUBLE)
    gnls_la = Column(DOUBLE)
    gnls_la_sd = Column(DOUBLE)
    gnls_lw = Column(DOUBLE)
    gnls_lw_sd = Column(DOUBLE)
    gnls_er = Column(DOUBLE)
    gnls_er_sd = Column(DOUBLE)
    gnls_aic = Column(DOUBLE)
    gnls_rmse = Column(DOUBLE)
    gnls_prob = Column(DOUBLE)
    nconc = Column(Integer, nullable=False)
    npts = Column(Integer, nullable=False)
    nrep = Column(DOUBLE, nullable=False)
    nmed_gtbl = Column(Integer, nullable=False)
    tmpi = Column(Integer, nullable=False)

    modified_by = Column(String(100), nullable=False)
    created_date = Column(DateTime, default=datetime.datetime.now, nullable=False)
    modified_date = Column(DateTime, default=datetime.datetime.now, nullable=False)