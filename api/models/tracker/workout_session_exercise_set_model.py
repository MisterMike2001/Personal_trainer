
from sqlalchemy import (
    Column,
    Integer,
    Numeric,
    DateTime,
    ForeignKey,
    UniqueConstraint,
    CheckConstraint,
)

from models.base import Base, IDMixin, TimestampMixin


class WorkoutSessionExerciseSet(Base, IDMixin, TimestampMixin):
    __tablename__ = "workout_session_exercise_set"
    __table_args__ = {"schema": "tracker"}
    
    workout_session_exercise_id = Column(
        Integer,
        ForeignKey(
            "tracker.workout_session_exercise.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    set_no = Column(
        Integer,
        nullable=False
    )

    reps_completed = Column(
        Integer,
        nullable=True
    )

    weight = Column(
        Numeric(7, 2),
        nullable=True
    )

    rpe = Column(
        Numeric(3, 1),
        nullable=True
    )

    rest_seconds = Column(
        Integer,
        nullable=True
    )

    completed_dt = Column(
        DateTime(timezone=True),
        nullable=True
    )

    __table_args__ = (
        UniqueConstraint(
            "workout_session_exercise_id",
            "set_no",
            name="uq_session_exercise_set"
        ),
        CheckConstraint(
            "set_no > 0",
            name="chk_session_set_number"
        ),
        CheckConstraint(
            "reps_completed IS NULL OR reps_completed >= 0",
            name="chk_session_set_reps"
        ),
        CheckConstraint(
            "weight IS NULL OR weight >= 0",
            name="chk_session_set_weight"
        ),
        CheckConstraint(
            "rpe IS NULL OR rpe BETWEEN 1 AND 10",
            name="chk_session_set_rpe"
        ),
        CheckConstraint(
            "rest_seconds IS NULL OR rest_seconds >= 0",
            name="chk_session_set_rest"
        ),
        {"schema": "tracker"}
    )
