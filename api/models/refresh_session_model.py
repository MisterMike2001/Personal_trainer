from sqlalchemy import Column, Integer, String, Boolean, DateTime, Identity, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class RefreshSession(Base):
    __tablename__ = 'refresh_session'
    __table_args__ = {'schema': 'auth'}

    id = Column(Integer, Identity(always=True), primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    token_hash = Column(String, nullable=False)
    expires_at = Column(DateTime(timezone=True), nullable=False)
    revoked_at = Column(DateTime(timezone=True), nullable=True)

    
    

