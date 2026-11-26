
from sqlalchemy import Column, String, Text

from models.base import Base, IDMixin


class MuscleGroup(Base, IDMixin):
    __tablename__ = "muscle_groups"
    __table_args__ = {"schema": "planning"}

    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=True)
