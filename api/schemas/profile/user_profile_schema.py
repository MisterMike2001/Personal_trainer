from pydantic import BaseModel
from datetime import datetime

class UserProfileBase(BaseModel):
    user_id : int
    gender:str
    date_of_birth: datetime
    height:float


class GetUserProfile(UserProfileBase):
    id :int
    create_dt: datetime

class CreateUserProfile(UserProfileBase):
    pass

class UpdateUserProfile(UserProfileBase):
    pass