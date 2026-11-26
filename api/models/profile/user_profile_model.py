
from sqlalchemy import (
    Column, Integer, String, Date, Numeric,
    DateTime, ForeignKey, func
)

from models.base import Base, IDMixin


class UserProfile(Base, IDMixin):
    __tablename__ = "user_profile"
    __table_args__ = {"schema": "profile"}

    user_id = Column(
        Integer,
        ForeignKey("auth.users.id", ondelete="CASCADE"),
        unique=True,
        nullable=False
    )

    gender = Column(String(30), nullable=True)
    date_of_birth = Column(Date, nullable=True)
    height = Column(Numeric(5, 2), nullable=False)

    create_dt = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )
