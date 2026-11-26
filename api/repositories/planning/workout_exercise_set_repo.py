from models.planning.workout_exercise_set_model import WorkoutExerciseSet
from schemas.planning.workout_exercise_set_schema import CreateWorkoutExerciseSet, UpdateWorkoutExerciseSet

class WorkoutExerciseSetRepository:
    def __init__(self, db):
        self.db = db

    def get_workout_exercise_sets(self, workout_exercise_id: int) -> list[WorkoutExerciseSet]:
        workout_exercise_sets = self.db.query(WorkoutExerciseSet).filter(WorkoutExerciseSet.workout_exercise_id == workout_exercise_id).order_by(WorkoutExerciseSet.set_no).all()
        return workout_exercise_sets

    def create_workout_exercise_set(self, workout_exercise_set: CreateWorkoutExerciseSet):
        new_workout_exercise_set = WorkoutExerciseSet(**workout_exercise_set.model_dump())
        self.db.add(new_workout_exercise_set)
        self.db.commit()
        self.db.refresh(new_workout_exercise_set)
        return new_workout_exercise_set

    def update_workout_exercise_set(self, updated_workout_exercise_set: UpdateWorkoutExerciseSet) -> WorkoutExerciseSet | None:
        old_workout_exercise_set = self.db.query(WorkoutExerciseSet).filter(WorkoutExerciseSet.id == updated_workout_exercise_set.id, WorkoutExerciseSet.workout_exercise_id == updated_workout_exercise_set.workout_exercise_id).first()

        if old_workout_exercise_set is None:
            return None

        changes = updated_workout_exercise_set.model_dump(exclude_unset=True, exclude={"id", "workout_exercise_id"})
        for field, value in changes.items():
            setattr(old_workout_exercise_set, field, value)

        self.db.commit()
        self.db.refresh(old_workout_exercise_set)
        return old_workout_exercise_set
