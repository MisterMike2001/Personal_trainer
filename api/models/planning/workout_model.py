
from sqlalchemy import (
    Column, Integer, String, Boolean,
    ForeignKey, UniqueConstraint,
    CheckConstraint, text
)

from models.base import Base, IDMixin, TimestampMixin


class Workout(Base, IDMixin, TimestampMixin):
    __tablename__ = "workout"
    __table_args__ = (
        UniqueConstraint("workout_plan_id", "order_no"),
        CheckConstraint("order_no > 0", name="order_positive"),
        CheckConstraint("cycle_day IS NULL OR cycle_day > 0", name="cycle_day_positive"),
        {"schema": "planning"},
    )

    workout_plan_id = Column(
        Integer,
        ForeignKey(
            "planning.workout_plan.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    name = Column(String(150), nullable=False)

    order_no = Column(Integer, nullable=False)
    cycle_day = Column(Integer, nullable=True)

    is_active = Column(
        Boolean,
        nullable=False,
        server_default=text("true")
    )
