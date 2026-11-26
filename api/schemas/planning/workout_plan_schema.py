from pydantic import BaseModel
from datetime import datetime

class WorkoutPlanBase(BaseModel):
    user_id: int
    name: str
    description: str | None = None
    cycle_length_days: int
    is_active: bool = True

class GetWorkoutPlan(WorkoutPlanBase):
    id: int
    create_dt: datetime

class CreateWorkoutPlan(WorkoutPlanBase):
    pass

class UpdateWorkoutPlan(WorkoutPlanBase):
    id: int
