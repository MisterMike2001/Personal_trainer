
from sqlalchemy import (
    Column, Integer, Numeric, DateTime,
    ForeignKey, func
)

from models.base import Base, IDMixin


class UserMeasurements(Base, IDMixin):
    __tablename__ = "user_measurements"
    __table_args__ = {"schema": "profile"}

    user_id = Column(
        Integer,
        ForeignKey("auth.users.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    chest = Column(Numeric(6, 2), nullable=True)
    waist = Column(Numeric(6, 2), nullable=True)
    hips = Column(Numeric(6, 2), nullable=True)
    shoulders = Column(Numeric(6, 2), nullable=True)
    arms = Column(Numeric(6, 2), nullable=True)
    thighs = Column(Numeric(6, 2), nullable=True)
    calves = Column(Numeric(6, 2), nullable=True)

    recorded_dt = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )

    create_dt = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )
