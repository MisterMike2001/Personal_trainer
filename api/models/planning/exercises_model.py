
from sqlalchemy import (
    Column, Integer, String, Text,
    Boolean, ForeignKey, text
)

from models.base import Base, IDMixin


class Exercise(Base, IDMixin):
    __tablename__ = "exercises"
    __table_args__ = {"schema": "planning"}

    name = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)

    motion_image_1 = Column(Text, nullable=True)
    motion_image_2 = Column(Text, nullable=True)

    equipment_id = Column(
        Integer,
        ForeignKey(
            "planning.equipment.id",
            ondelete="SET NULL"
        ),
        nullable=True
    )

    is_active = Column(
        Boolean,
        nullable=False,
        server_default=text("true")
    )
