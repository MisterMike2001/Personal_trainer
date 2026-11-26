from models.profile.user_weight_model import UserWeight
from schemas.profile.user_weight_schem import CreateUserWeight, GetUserWeight


class UserWeightReporitory:
    def __init__(self, db):
        self.db = db

    def get_user_weights(self, user_id)->list[GetUserWeight]:
        user_weights = self.db.query(UserWeight).filter(UserWeight.user_id == user_id).all()
        return user_weights
    
    def get_latest_user_weight(self, user_id: int)->GetUserWeight:
        user_weight = self.db.query(UserWeight).filter(UserWeight.user_id == user_id).order_by(UserWeight.create_dt.desc()).first()
        return user_weight
    
    def create_user_weight(self, user_weight: CreateUserWeight):
        weight = UserWeight(**user_weight.model_dump())

        self.db.add(weight)
        self.db.commit()
        self.db.refresh(weight)

        return weight