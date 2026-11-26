from models.planning.equipement_model import Equipment
from schemas.planning.equipment_schema import CreateEquipment, UpdateEquipment

class EquipmentRepository:
    def __init__(self, db):
        self.db = db

    def get_equipment(self) -> list[Equipment]:
        equipment = self.db.query(Equipment).all()
        return equipment

    def create_equipment(self, equipment: CreateEquipment):
        new_equipment = Equipment(**equipment.model_dump())
        self.db.add(new_equipment)
        self.db.commit()
        self.db.refresh(new_equipment)
        return new_equipment

    def update_equipment(self, updated_equipment: UpdateEquipment) -> Equipment | None:
        old_equipment = self.db.query(Equipment).filter(Equipment.id == updated_equipment.id).first()

        if old_equipment is None:
            return None

        changes = updated_equipment.model_dump(exclude_unset=True, exclude={"id"})
        for field, value in changes.items():
            setattr(old_equipment, field, value)

        self.db.commit()
        self.db.refresh(old_equipment)
        return old_equipment
