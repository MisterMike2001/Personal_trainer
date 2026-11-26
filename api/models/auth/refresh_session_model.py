from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from models.base import Base, IDMixin


class RefreshSession(Base, IDMixin):
    __tablename__ = 'refresh_session'
    __table_args__ = {'schema': 'auth'}

    user_id = Column(Integer, ForeignKey("auth.users.id", ondelete="CASCADE"), nullable=False, index=True)
    token_hash = Column(String(64), nullable=False, unique=True)
    expires_at = Column(DateTime(timezone=True), nullable=False)
    revoked_at = Column(DateTime(timezone=True), nullable=True)

    
    

