import datetime

from database.chemprop.endpoints import Endpoints
from database.chemprop.parameters import Parameters
from database.database_schemas import Schemas
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base


class EndpointAcceptableParameters(Base):
    """Maps to endpoint_acceptable_parameters table in chemprop databases."""

    __tablename__ = "endpoint_acceptable_parameters"
    __table_args__ = {'schema': Schemas.chemprop_schema}

    id = Column(Integer, primary_key=True, nullable=False)
    fk_endpoint_id = Column(ForeignKey(Endpoints.id))
    fk_parameter_id = Column(ForeignKey(Parameters.id))
    created_by = Column(String(255), nullable=False)
    updated_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now, nullable=False)

    endpoint = relationship("Endpoints")
    parameter = relationship("Parameters")
