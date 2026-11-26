
from datetime import datetime
from pydantic import BaseModel, EmailStr, ConfigDict, Field

class RefreshSessionSchema(BaseModel):
    id: int
    user_id: int
    token_hash: str
    expires_at: datetime
    revoked_at: datetime | None = None

class RefreshSessionCreateSchema(BaseModel):
    user_id: int
    token_hash: str
    expires_at: datetime
    revoked_at: datetime | None = None

