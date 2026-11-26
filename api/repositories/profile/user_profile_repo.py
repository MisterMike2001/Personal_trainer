from models.profile.user_profile_model import UserProfile
from schemas.profile.user_profile_schema import CreateUserProfile, UpdateUserProfile, GetUserProfile

class UserProfileRepository:
    def __init__(self,db):
        self.db =db

    def get_user_profile(self, user_id : int)->GetUserProfile:
        user_profile = self.db.query(UserProfile).filter(UserProfile.user_id == user_id).first()
        return user_profile
    
    def create_user_profile(self, user_profile: CreateUserProfile):

        profile = UserProfile(**user_profile.model_dump())
        self.db.add(profile)
        self.db.commit()
        self.db.refresh(profile)

        return profile

    def update_user_dprofile(self,updated_user_proflile: UpdateUserProfile)->GetUserProfile:
        old_user_profile = self.get_user_profile(user_id=updated_user_proflile.user_id)

        if not old_user_profile:
            return None
        
        changes = updated_user_proflile.model_dump(exclude_unset = True)

        for field, value in changes.items():
            setattr(old_user_profile,field,value)
        
        self.db.commit()
        self.db.refresh(old_user_profile)
        return old_user_profile

