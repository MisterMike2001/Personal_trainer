from models.profile.user_measurements_model import UserMeasurements
from schemas.profile.user_measuremnets_schema import CreateUserMeasurements,GetUserMeasurements

class UserMeasurementsRepository:
    def __init__(self,db):
        self.db = db

    def get_user_measurements(self, user_id:int)-> list[GetUserMeasurements]:
        user_measurements = self.db.query(UserMeasurements).filter(UserMeasurements.user_id == user_id).all()
        return user_measurements
    
    def get_latest_user_measurements(self,user_id:int)->GetUserMeasurements:
        user_measurement = self.db.query(UserMeasurements).filter(UserMeasurements.user_id == user_id).order_by(UserMeasurements.create_dt.desc()).first()
        return user_measurement
    
    def create_user_measurements(self, user_measurement: CreateUserMeasurements):
        measurements = UserMeasurements(**user_measurement.model_dump())
        self.db.add(measurements)
        self.db.commit()
        self.db.refresh(measurements)

        return measurements