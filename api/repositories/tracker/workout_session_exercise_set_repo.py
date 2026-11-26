from models.tracker.workout_session_exercise_set_model import WorkoutSessionExerciseSet
from schemas.tracker.workout_session_exercise_set_schema import GetWorkoutSessionExerciseSet, CreateWorkoutSessionExerciseSet

class WorkoutSessionExerciseSetRepository:
    def __init__(self,db):
        self.db = db

    def get_workout_session_exercise_sets(self, workout_session_exercise_id:int) -> list[GetWorkoutSessionExerciseSet]:
        exercise_sets = self.db.query(WorkoutSessionExerciseSet).filter(WorkoutSessionExerciseSet.workout_session_exercise_id == workout_session_exercise_id).all()
        return exercise_sets

    def create_workout_session_exercise_set(self, workout_exercise_set: CreateWorkoutSessionExerciseSet):
        exercise_set = WorkoutSessionExerciseSet(**workout_exercise_set.model_dump())
        self.db.add(exercise_set)
        self.db.commit()
        self.db.refresh(exercise_set)
        return exercise_set
