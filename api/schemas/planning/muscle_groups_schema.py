from pydantic import BaseModel

class MuscleGroupBase(BaseModel):
    name: str
    description: str | None = None

class GetMuscleGroup(MuscleGroupBase):
    id: int

class CreateMuscleGroup(MuscleGroupBase):
    pass

class UpdateMuscleGroup(MuscleGroupBase):
    id: int
