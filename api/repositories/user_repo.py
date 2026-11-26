
from schemas.users_schema import UserCreate, UserUpdate
from models.auth.users_model import User


class UserRepository:
    def __init__(self, db):
        self.db = db

    def get_user_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()
    
    def get_user_by_id(self, user_id: int) -> User | None:
        return self.db.query(User).filter(User.id ==user_id).first()

    def add_user(self, user: UserCreate):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user
    
    def update_user(self, user: UserUpdate):
        old_user = self.get_user_by_id(user.id)

        if not old_user:
            return None
        changes = user.model_dump(exclude_unset=True)

        for field, value in changes.items():
            setattr(old_user, field, value)

        self.db.commit()
        self.db.refresh(old_user)
        return old_user