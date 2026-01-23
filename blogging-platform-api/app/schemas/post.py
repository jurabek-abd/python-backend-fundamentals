from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class PostCreate(BaseModel):
    title: str = Field(min_length=5, max_length=255)
    content: str = Field(min_length=5, max_length=50000)
    category: Optional[str] = None
    tags: Optional[list[str]] = []


class PostUpdate(BaseModel):
    title: Optional[str] = Field(min_length=5, max_length=255)
    content: Optional[str] = Field(min_length=5, max_length=50000)
    category: Optional[str] = None
    tags: Optional[list[str]] = []


class PostOut(BaseModel):
    id: str
    title: str
    content: str
    category: Optional[str] = None
    tags: Optional[list[str]] = []
    created_at: datetime
    updated_at: datetime | None

    class Config:
        from_attributes = True
