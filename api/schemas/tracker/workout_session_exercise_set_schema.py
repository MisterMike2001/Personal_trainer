from pydantic import BaseModel
from datetime import datetime

class WorkoutSessionExerciseSetBase(BaseModel):
    workout_session_exercise_id : int
    set_no :int
    reps_completed :int
    weight :float
    rpe :float
    rest_seconds :int
    completed_dt :datetime

class GetWorkoutSessionExerciseSet(WorkoutSessionExerciseSetBase):
    id:int


class CreateWorkoutSessionExerciseSet(WorkoutSessionExerciseSetBase):
    pass


class UpdateWorkoutSessionExerciseSet(WorkoutSessionExerciseSetBase):
    pass