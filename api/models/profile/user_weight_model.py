
from sqlalchemy import (
    Column, Integer, Numeric, DateTime,
    ForeignKey, func
)

from models.base import Base, IDMixin


class UserWeight(Base, IDMixin):
    __tablename__ = "user_weight"
    __table_args__ = {"schema": "profile"}

    user_id = Column(
        Integer,
        ForeignKey("auth.users.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    weight = Column(Numeric(6, 2), nullable=False)

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
