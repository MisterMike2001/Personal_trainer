from pydantic import BaseModel
from datetime import datetime

class WorkoutSessionBase(BaseModel):
    user_id:int
    workout_id:int
    start_dt:datetime
    end_dt:datetime | None
    status: str

class GetWorkoutSession(WorkoutSessionBase):
    id:int

class CreateWorkoutSession(WorkoutSessionBase):
    pass

class UpdateWorkoutSession(WorkoutSessionBase):
    id:int