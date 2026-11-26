
from sqlalchemy import (
    Column, Integer, ForeignKey,
    UniqueConstraint, CheckConstraint
)

from models.base import Base, IDMixin, TimestampMixin


class WorkoutExercise(Base, IDMixin, TimestampMixin):
    __tablename__ = "workout_exercise"
    __table_args__ = (
        UniqueConstraint("workout_id", "exercise_order"),
        CheckConstraint("exercise_order > 0", name="exercise_order_positive"),
        {"schema": "planning"},
    )

    workout_id = Column(
        Integer,
        ForeignKey(
            "planning.workout.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    exercise_id = Column(
        Integer,
        ForeignKey("planning.exercises.id"),
        nullable=False
    )

    exercise_order = Column(Integer, nullable=False)
