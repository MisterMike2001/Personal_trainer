from sqlalchemy import Column, String, Boolean, DateTime, func

from models.base import Base, IDMixin


class User(Base, IDMixin):
    __tablename__ = "users"
    __table_args__ = {"schema": "auth"}

    name = Column(String(100), nullable=False)
    surname = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    cell = Column(String(20), nullable=False)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)
    create_dt = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
