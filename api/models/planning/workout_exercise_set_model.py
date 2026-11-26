
from sqlalchemy import (
    Column, Integer, String, Numeric,
    ForeignKey, UniqueConstraint,
    CheckConstraint, text
)

from models.base import Base, IDMixin, TimestampMixin


class WorkoutExerciseSet(Base, IDMixin, TimestampMixin):
    __tablename__ = "workout_exercise_set"
    __table_args__ = (
        UniqueConstraint("workout_exercise_id", "set_no"),
        CheckConstraint("set_no > 0", name="set_no_positive"),
        CheckConstraint("target_reps_min IS NULL OR target_reps_min >= 0", name="reps_min_nonnegative"),
        CheckConstraint("target_reps_max IS NULL OR target_reps_max >= 0", name="reps_max_nonnegative"),
        CheckConstraint("target_reps_min IS NULL OR target_reps_max IS NULL OR target_reps_min <= target_reps_max", name="reps_range_valid"),
        CheckConstraint("target_weight IS NULL OR target_weight >= 0", name="weight_nonnegative"),
        CheckConstraint("rest_seconds IS NULL OR rest_seconds >= 0", name="rest_nonnegative"),
        {"schema": "planning"},
    )

    workout_exercise_id = Column(
        Integer,
        ForeignKey(
            "planning.workout_exercise.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    set_no = Column(Integer, nullable=False)

    target_reps_min = Column(Integer, nullable=True)
    target_reps_max = Column(Integer, nullable=True)

    target_weight = Column(Numeric(7, 2), nullable=True)

    rest_seconds = Column(Integer, nullable=True)

    set_type = Column(
        String(30),
        nullable=False,
        server_default=text("'working'")
    )
