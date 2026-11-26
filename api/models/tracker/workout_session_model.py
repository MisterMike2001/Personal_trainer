
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    CheckConstraint,
    Index,
    text,
    func,
)

from models.base import Base, IDMixin, TimestampMixin


class WorkoutSession(Base, IDMixin, TimestampMixin):
    __tablename__ = "workout_session"
    __table_args__ = {"schema": "tracker"}
    
    user_id = Column(
        Integer,
        ForeignKey(
            "auth.users.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    workout_id = Column(
        Integer,
        ForeignKey(
            "planning.workout.id",
            ondelete="SET NULL"
        ),
        nullable=True
    )

    start_dt = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )

    end_dt = Column(
        DateTime(timezone=True),
        nullable=True
    )

    status = Column(
        String(20),
        nullable=False,
        server_default=text("'in_progress'")
    )

    __table_args__ = (
        CheckConstraint(
            "status IN ('in_progress', 'completed', 'cancelled')",
            name="chk_workout_session_status"
        ),
        CheckConstraint(
            "end_dt IS NULL OR end_dt >= start_dt",
            name="chk_workout_session_dates"
        ),
        Index(
            "idx_workout_session_user_date",
            user_id,
            start_dt.desc()
        ),
        Index(
            "idx_workout_session_workout",
            workout_id
        ),
        {"schema": "tracker"}
    )
