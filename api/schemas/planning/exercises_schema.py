from pydantic import BaseModel

class ExerciseBase(BaseModel):
    name: str
    description: str | None = None
    motion_image_1: str | None = None
    motion_image_2: str | None = None
    equipment_id: int | None = None
    is_active: bool = True

class GetExercise(ExerciseBase):
    id: int

class CreateExercise(ExerciseBase):
    pass

class UpdateExercise(ExerciseBase):
    id: int
