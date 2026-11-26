from models.planning.workout_exercises_model import WorkoutExercise
from schemas.planning.workout_exercises_schema import CreateWorkoutExercise, UpdateWorkoutExercise

class WorkoutExerciseRepository:
    def __init__(self, db):
        self.db = db

    def get_workout_exercises(self, workout_id: int) -> list[WorkoutExercise]:
        workout_exercises = self.db.query(WorkoutExercise).filter(WorkoutExercise.workout_id == workout_id).order_by(WorkoutExercise.exercise_order).all()
        return workout_exercises

    def create_workout_exercise(self, workout_exercise: CreateWorkoutExercise):
        new_workout_exercise = WorkoutExercise(**workout_exercise.model_dump())
        self.db.add(new_workout_exercise)
        self.db.commit()
        self.db.refresh(new_workout_exercise)
        return new_workout_exercise

    def update_workout_exercise(self, updated_workout_exercise: UpdateWorkoutExercise) -> WorkoutExercise | None:
        old_workout_exercise = self.db.query(WorkoutExercise).filter(WorkoutExercise.id == updated_workout_exercise.id, WorkoutExercise.workout_id == updated_workout_exercise.workout_id).first()

        if old_workout_exercise is None:
            return None

        changes = updated_workout_exercise.model_dump(exclude_unset=True, exclude={"id", "workout_id"})
        for field, value in changes.items():
            setattr(old_workout_exercise, field, value)

        self.db.commit()
        self.db.refresh(old_workout_exercise)
        return old_workout_exercise
