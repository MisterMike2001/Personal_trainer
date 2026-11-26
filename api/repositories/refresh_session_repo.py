


from models.auth.refresh_session_model import RefreshSession
from schemas.refresh_session_schema import RefreshSessionSchema, RefreshSessionCreateSchema


class RefreshSessionRepo:
    def __init__(self, db):
        self.db = db

    def get_refresh_token(self, token_hash: str):
        return self.db.query(RefreshSession).filter(RefreshSession.token_hash == token_hash).first()
    

    def create_refresh_session(self, refresh_token: RefreshSessionCreateSchema):
        session = RefreshSession(**refresh_token.model_dump())
        self.db.add(session)
        self.db.commit()
        self.db.refresh(session)
        return session
    
    def update_refresh_session(self, refresh_token: RefreshSessionSchema, old_token_hash: str):
        existing_token = self.get_refresh_token(old_token_hash)
        if existing_token:
            for field, value in refresh_token.model_dump(exclude_unset=True).items():
                setattr(existing_token, field, value)
            self.db.commit()
            self.db.refresh(existing_token)
            return existing_token
        return None
    
    def delete_refresh_session(self, refresh_token: str):
        refresh_session = self.get_refresh_token(refresh_token)
        if refresh_session:
            self.db.delete(refresh_session)
            self.db.commit()
            return True
        return False