
from sqlalchemy import (
    Column, Integer, ForeignKey, UniqueConstraint
)

from models.base import Base, IDMixin, TimestampMixin


class WorkoutMuscleGroup(Base, IDMixin, TimestampMixin):
    __tablename__ = "workout_muscle_groups"
    __table_args__ = (
        UniqueConstraint("workout_id", "muscle_group_id"),
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

    muscle_group_id = Column(
        Integer,
        ForeignKey(
            "planning.muscle_groups.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )
