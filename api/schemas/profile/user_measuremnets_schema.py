from pydantic import BaseModel
from datetime import datetime

class UserMeasurementsBase(BaseModel):
    user_id : int
    chest: float
    waist:float
    hips:float
    shoulders: float
    arms: float
    thighs:float
    calves:float


class GetUserMeasurements(UserMeasurementsBase):
    id :int
    recorded_dt:datetime
    create_dt: datetime

class CreateUserMeasurements(UserMeasurementsBase):
    pass

class UpdateUserMeasurements(UserMeasurementsBase):
    pass