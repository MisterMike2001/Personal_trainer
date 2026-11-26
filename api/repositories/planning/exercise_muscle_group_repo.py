from models.planning.excersise_mussle_groups_model import ExerciseMuscleGroup
from schemas.planning.exercise_muscle_group_schema import CreateExerciseMuscleGroup, UpdateExerciseMuscleGroup

class ExerciseMuscleGroupRepository:
    def __init__(self, db):
        self.db = db

    def get_exercise_muscle_groups(self, exercise_id: int) -> list[ExerciseMuscleGroup]:
        exercise_muscle_groups = self.db.query(ExerciseMuscleGroup).filter(ExerciseMuscleGroup.exercise_id == exercise_id).all()
        return exercise_muscle_groups

    def create_exercise_muscle_group(self, exercise_muscle_group: CreateExerciseMuscleGroup):
        new_exercise_muscle_group = ExerciseMuscleGroup(**exercise_muscle_group.model_dump())
        self.db.add(new_exercise_muscle_group)
        self.db.commit()
        self.db.refresh(new_exercise_muscle_group)
        return new_exercise_muscle_group

    def update_exercise_muscle_group(self, updated_exercise_muscle_group: UpdateExerciseMuscleGroup) -> ExerciseMuscleGroup | None:
        old_exercise_muscle_group = self.db.query(ExerciseMuscleGroup).filter(ExerciseMuscleGroup.id == updated_exercise_muscle_group.id, ExerciseMuscleGroup.exercise_id == updated_exercise_muscle_group.exercise_id).first()

        if old_exercise_muscle_group is None:
            return None

        changes = updated_exercise_muscle_group.model_dump(exclude_unset=True, exclude={"id", "exercise_id"})
        for field, value in changes.items():
            setattr(old_exercise_muscle_group, field, value)

        self.db.commit()
        self.db.refresh(old_exercise_muscle_group)
        return old_exercise_muscle_group
