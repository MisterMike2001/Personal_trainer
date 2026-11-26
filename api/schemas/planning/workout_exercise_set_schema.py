from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal

class WorkoutExerciseSetBase(BaseModel):
    workout_exercise_id: int
    set_no: int
    target_reps_min: int | None = None
    target_reps_max: int | None = None
    target_weight: Decimal | None = None
    rest_seconds: int | None = None
    set_type: str = "working"

class GetWorkoutExerciseSet(WorkoutExerciseSetBase):
    id: int
    create_dt: datetime

class CreateWorkoutExerciseSet(WorkoutExerciseSetBase):
    pass

class UpdateWorkoutExerciseSet(WorkoutExerciseSetBase):
    id: int
