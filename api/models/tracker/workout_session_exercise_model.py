
from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    UniqueConstraint,
    CheckConstraint,
    Index,
)

from models.base import Base, IDMixin, TimestampMixin


class WorkoutSessionExercise(Base, IDMixin, TimestampMixin):
    __tablename__ = "workout_session_exercise"
    __table_args__ = {"schema": "tracker"}

    workout_session_id = Column(
        Integer,
        ForeignKey(
            "tracker.workout_session.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    exercise_id = Column(
        Integer,
        ForeignKey(
            "planning.exercises.id",
            ondelete="RESTRICT"
        ),
        nullable=False
    )

    workout_exercise_id = Column(
        Integer,
        ForeignKey(
            "planning.workout_exercise.id",
            ondelete="SET NULL"
        ),
        nullable=True
    )

    exercise_order = Column(
        Integer,
        nullable=False
    )

    __table_args__ = (
        UniqueConstraint(
            "workout_session_id",
            "exercise_order",
            name="uq_session_exercise_order"
        ),
        CheckConstraint(
            "exercise_order > 0",
            name="chk_session_exercise_order"
        ),
        Index(
            "idx_session_exercise_exercise",
            exercise_id
        ),
        Index(
            "idx_session_exercise_planned",
            workout_exercise_id
        ),
        {"schema": "tracker"}
    )
