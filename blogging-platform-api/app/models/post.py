import uuid
from datetime import datetime
from typing import Optional

from database.db import Base
from sqlalchemy import JSON, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, validates


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[str] = mapped_column(
        String(30), primary_key=True, default=lambda: str(uuid.uuid4()), index=True
    )
    title: Mapped[str] = mapped_column(String(255))
    content: Mapped[str] = mapped_column(Text)
    category: Mapped[Optional[str]] = mapped_column(String(100))
    tags: Mapped[list] = mapped_column(JSON, default=list)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[Optional[datetime]] = mapped_column(
        default=None, onupdate=func.now()
    )

    @validates("tags")
    def validate_tags(self, key, value):
        # Changed: _ → key (it's the column name, might be useful)
        if value is None:
            return []

        if not isinstance(value, list):
            raise ValueError("Tags must be a list")

        for tag in value:
            if not isinstance(tag, str):
                raise ValueError("All tags must be strings")
            if len(tag) > 50:
                raise ValueError(f"Tag '{tag}' exceeds 50 characters")
            if len(tag) < 3:
                raise ValueError(f"Tag '{tag}' must be at least 3 characters")

        return value
