from pydantic import BaseModel
from datetime import datetime

class WorkoutExerciseBase(BaseModel):
    workout_id: int
    exercise_id: int
    exercise_order: int

class GetWorkoutExercise(WorkoutExerciseBase):
    id: int
    create_dt: datetime

class CreateWorkoutExercise(WorkoutExerciseBase):
    pass

class UpdateWorkoutExercise(WorkoutExerciseBase):
    id: int
