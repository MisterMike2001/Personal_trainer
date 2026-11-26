from pydantic import BaseModel
from datetime import datetime

class WorkoutSessionExercisesBase(BaseModel):
    workout_session_id :int
    exercise_id :int
    workout_exercise_id :int
    exercise_order : int


class GetWorkoutSessionExercises(WorkoutSessionExercisesBase):
    id:int 

class CreateWorkoutSessionExercises(WorkoutSessionExercisesBase):
    pass 

class UpdateWorkoutSessionExercises(WorkoutSessionExercisesBase):
    pass