
from sqlalchemy import (
    Column, Integer, String, Text,
    Boolean, ForeignKey, CheckConstraint, text
)

from models.base import Base, IDMixin, TimestampMixin


class WorkoutPlan(Base, IDMixin, TimestampMixin):
    __tablename__ = "workout_plan"
    __table_args__ = (
        CheckConstraint("cycle_length_days > 0", name="cycle_length_positive"),
        {"schema": "planning"},
    )

    user_id = Column(
        Integer,
        ForeignKey(
            "auth.users.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    name = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)

    cycle_length_days = Column(
        Integer,
        nullable=False
    )

    is_active = Column(
        Boolean,
        nullable=False,
        server_default=text("true")
    )
