import uuid

from database.db import Base
from sqlalchemy import Column, DateTime, String, Text
from sqlalchemy.sql import func


class Post(Base):
    __tablename__ = "posts"

    id = Column(
        String(30), primary_key=True, default=lambda: str(uuid.uuid4()), index=True
    )
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    category = Column(String(100))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
