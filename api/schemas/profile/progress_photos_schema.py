from datetime import datetime
from pydantic import BaseModel

class ProgressPhotosBase(BaseModel):
    user_id:int
    front : str
    back : str
    left_side : str
    right_side : str


class GetProgressPhotos(ProgressPhotosBase):
    id :int
    recorded_dt : datetime
    create_dt : datetime

class CreateProgessPhotos(ProgressPhotosBase):
    pass

class UpdateProgressPhotos(ProgressPhotosBase):
    pass