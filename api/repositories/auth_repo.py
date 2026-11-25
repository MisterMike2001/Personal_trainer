

from datetime import datetime, timedelta, timezone
from schemas.refresh_session_schema import RefreshSessionCreateSchema, RefreshSessionSchema
from repositories.refresh_session_repo import RefreshSessionRepo
from core.tokens import create_access_token, create_refresh_token, hash_refresh_token
from repositories.user_repo import UserRepository
import bcrypt
from schemas.users_schema import UserLogin


class AuthRepository:
    def __init__(self, db):
        self.db = db
        self.user_repo = UserRepository(db)
        self.refresh_session_repo = RefreshSessionRepo(db)

    def authenticate_user(self, login_user: UserLogin):
        user = self.user_repo.get_user_by_email(login_user.email)

        if not user:
            return None
        
        if not self.verify_password(login_user.password, user.password):
            raise ValueError("Invalid password")
        

        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token()  # Placeholder for refresh token generation
        refresh_token_hashed = hash_refresh_token(refresh_token)  # Hash the refresh token before storing

        # Create a new refresh session
        refresh_session = RefreshSessionCreateSchema(
            user_id=user.id,
            token_hash=refresh_token_hashed,
            expires_at=datetime.now(timezone.utc)+ timedelta(days=30),  # Set expiration date
            revoked_at=None
        )
        self.refresh_session_repo.create_refresh_session(refresh_session)

        tokens = {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
            "expires_in": 900,
        }
        return tokens

    def verify_password(self, plain_password, hashed_password) -> bool:
        return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))
    

    def refresh_access_token(self, refresh_token: str):
        old_refresh_token_hashed = hash_refresh_token(refresh_token)
        old_refresh_session = self.refresh_session_repo.get_refresh_token(old_refresh_token_hashed)

        if not old_refresh_session:
            raise ValueError("Invalid refresh token")

        if old_refresh_session.revoked_at is not None:
            raise ValueError("Refresh token has been revoked")

        if old_refresh_session.expires_at <= datetime.now(timezone.utc):
            raise ValueError("Refresh token has expired")

        user = self.user_repo.get_user_by_id(old_refresh_session.user_id)
        if not user:
            raise ValueError("User not found")

        new_access_token = create_access_token(user.id)
        refresh_token = create_refresh_token()  # Generate a new refresh token
        refresh_token_hashed = hash_refresh_token(refresh_token)  # Hash the new refresh token


        # Create a new refresh session
        refresh_session = RefreshSessionCreateSchema(
            user_id=user.id,
            token_hash=refresh_token_hashed,
            expires_at=datetime.now(timezone.utc)+ timedelta(days=30),  # Set expiration date
            revoked_at=None
        )
        self.refresh_session_repo.update_refresh_session(refresh_session, old_refresh_token_hashed)


        tokens ={
            "access_token": new_access_token,
            "refresh_token": refresh_token,
            "refresh_token_hashed": refresh_token_hashed
        }


        return tokens
    
    def revoke_refresh_token(self, refresh_token: str) -> bool:
        token_hash = hash_refresh_token(refresh_token)
        refresh_session = self.refresh_session_repo.get_refresh_token(token_hash)

        if refresh_session is None:
            return True

        if refresh_session.revoked_at is not None:
            return True

        try:
            refresh_session.revoked_at = datetime.now(timezone.utc)
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            raise
