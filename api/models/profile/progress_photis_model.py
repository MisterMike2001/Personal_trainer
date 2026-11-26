from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func

from models.base import Base, IDMixin


class ProgressPhoto(Base, IDMixin):
    __tablename__ = "progress_photos"
    __table_args__ = {"schema": "profile"}

    user_id = Column(Integer, ForeignKey("auth.users.id", ondelete="CASCADE"), index=True, nullable=False)
    front = Column(String, nullable=False)
    back = Column(String, nullable=False)
    left_side = Column(String, nullable=False)
    right_side = Column(String, nullable=False)
    recorded_dt = Column(DateTime(timezone=True), nullable=True)
    create_dt = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
