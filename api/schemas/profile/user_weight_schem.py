from pydantic import BaseModel
from datetime import datetime

class UserWeightBase(BaseModel):
    user_id : int
    weight: float


class GetUserWeight(UserWeightBase):
    id :int
    recorded_dt:datetime
    create_dt:datetime

class CreateUserWeight(UserWeightBase):
    pass

class UpdateUserWeight(UserWeightBase):
    pass

