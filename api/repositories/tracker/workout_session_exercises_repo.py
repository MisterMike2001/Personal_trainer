from models.tracker.workout_session_exercise_model import WorkoutSessionExercise
from schemas.tracker.workout_session_exercises_schema import GetWorkoutSessionExercises, CreateWorkoutSessionExercises

class WorkoutSessionExerciseRepository:
    def __init__(self,db):
        self.db= db

    def get_workout_session_exercises(self, workout_session_id:int) -> list[GetWorkoutSessionExercises]:
        exercises = self.db.query(WorkoutSessionExercise).filter(WorkoutSessionExercise.workout_session_id == workout_session_id).all()
        return exercises
    
    def create_workout_session_exercise(self , workout_exercise: CreateWorkoutSessionExercises):
        exercise = WorkoutSessionExercise(** workout_exercise.model_dump())
        self.db.add(exercise)
        self.db.commit()
        self.db.refresh(exercise)
        return exercise