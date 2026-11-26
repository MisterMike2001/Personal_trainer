from pydantic import BaseModel

class EquipmentBase(BaseModel):
    name: str
    description: str | None = None
    image: str | None = None
    is_active: bool = True

class GetEquipment(EquipmentBase):
    id: int

class CreateEquipment(EquipmentBase):
    pass

class UpdateEquipment(EquipmentBase):
    id: int
