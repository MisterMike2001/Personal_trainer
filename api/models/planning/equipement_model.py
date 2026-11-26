
from sqlalchemy import Column, String, Text, Boolean, text

from models.base import Base, IDMixin


class Equipment(Base, IDMixin):
    __tablename__ = "equipment"
    __table_args__ = {"schema": "planning"}

    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    image = Column(Text, nullable=True)

    is_active = Column(
        Boolean,
        nullable=False,
        server_default=text("true")
    )
   