from pydantic import BaseModel
from datetime import datetime

class WorkoutMuscleGroupBase(BaseModel):
    workout_id: int
    muscle_group_id: int

class GetWorkoutMuscleGroup(WorkoutMuscleGroupBase):
    id: int
    create_dt: datetime

class CreateWorkoutMuscleGroup(WorkoutMuscleGroupBase):
    pass

class UpdateWorkoutMuscleGroup(WorkoutMuscleGroupBase):
    id: int
