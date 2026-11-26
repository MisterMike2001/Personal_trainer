from pydantic import BaseModel
from datetime import datetime

class WorkoutBase(BaseModel):
    workout_plan_id: int
    name: str
    order_no: int
    cycle_day: int | None = None
    is_active: bool = True

class GetWorkout(WorkoutBase):
    id: int
    create_dt: datetime

class CreateWorkout(WorkoutBase):
    pass

class UpdateWorkout(WorkoutBase):
    id: int
