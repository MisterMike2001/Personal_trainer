
from sqlalchemy import (
    Column, Integer, ForeignKey, UniqueConstraint
)

from models.base import Base, IDMixin, TimestampMixin


class ExerciseMuscleGroup(Base, IDMixin, TimestampMixin):
    __tablename__ = "exercise_muscle_groups"
    __table_args__ = (
        UniqueConstraint("exercise_id", "muscle_group_id"),
        {"schema": "planning"},
    )

    exercise_id = Column(
        Integer,
        ForeignKey(
            "planning.exercises.id",
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
