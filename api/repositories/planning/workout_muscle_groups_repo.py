from models.planning.workout_muscle_groups_model import WorkoutMuscleGroup
from schemas.planning.workout_muscle_groups_schema import CreateWorkoutMuscleGroup, UpdateWorkoutMuscleGroup

class WorkoutMuscleGroupRepository:
    def __init__(self, db):
        self.db = db

    def get_workout_muscle_groups(self, workout_id: int) -> list[WorkoutMuscleGroup]:
        workout_muscle_groups = self.db.query(WorkoutMuscleGroup).filter(WorkoutMuscleGroup.workout_id == workout_id).all()
        return workout_muscle_groups

    def create_workout_muscle_group(self, workout_muscle_group: CreateWorkoutMuscleGroup):
        new_workout_muscle_group = WorkoutMuscleGroup(**workout_muscle_group.model_dump())
        self.db.add(new_workout_muscle_group)
        self.db.commit()
        self.db.refresh(new_workout_muscle_group)
        return new_workout_muscle_group

    def update_workout_muscle_group(self, updated_workout_muscle_group: UpdateWorkoutMuscleGroup) -> WorkoutMuscleGroup | None:
        old_workout_muscle_group = self.db.query(WorkoutMuscleGroup).filter(WorkoutMuscleGroup.id == updated_workout_muscle_group.id, WorkoutMuscleGroup.workout_id == updated_workout_muscle_group.workout_id).first()

        if old_workout_muscle_group is None:
            return None

        changes = updated_workout_muscle_group.model_dump(exclude_unset=True, exclude={"id", "workout_id"})
        for field, value in changes.items():
            setattr(old_workout_muscle_group, field, value)

        self.db.commit()
        self.db.refresh(old_workout_muscle_group)
        return old_workout_muscle_group
