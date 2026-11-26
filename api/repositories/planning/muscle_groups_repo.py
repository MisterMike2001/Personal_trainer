from models.planning.muscle_groups_model import MuscleGroup
from schemas.planning.muscle_groups_schema import CreateMuscleGroup, UpdateMuscleGroup

class MuscleGroupRepository:
    def __init__(self, db):
        self.db = db

    def get_muscle_groups(self) -> list[MuscleGroup]:
        muscle_groups = self.db.query(MuscleGroup).all()
        return muscle_groups

    def create_muscle_group(self, muscle_group: CreateMuscleGroup):
        new_muscle_group = MuscleGroup(**muscle_group.model_dump())
        self.db.add(new_muscle_group)
        self.db.commit()
        self.db.refresh(new_muscle_group)
        return new_muscle_group

    def update_muscle_group(self, updated_muscle_group: UpdateMuscleGroup) -> MuscleGroup | None:
        old_muscle_group = self.db.query(MuscleGroup).filter(MuscleGroup.id == updated_muscle_group.id).first()

        if old_muscle_group is None:
            return None

        changes = updated_muscle_group.model_dump(exclude_unset=True, exclude={"id"})
        for field, value in changes.items():
            setattr(old_muscle_group, field, value)

        self.db.commit()
        self.db.refresh(old_muscle_group)
        return old_muscle_group
