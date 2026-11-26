from pydantic import BaseModel
from datetime import datetime

class ExerciseMuscleGroupBase(BaseModel):
    exercise_id: int
    muscle_group_id: int

class GetExerciseMuscleGroup(ExerciseMuscleGroupBase):
    id: int
    create_dt: datetime

class CreateExerciseMuscleGroup(ExerciseMuscleGroupBase):
    pass

class UpdateExerciseMuscleGroup(ExerciseMuscleGroupBase):
    id: int
