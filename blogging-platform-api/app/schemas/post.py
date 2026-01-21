from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class PostCreate(BaseModel):
    title: str = Field(min_length=5, max_length=255)
    content: str = Field(min_length=5, max_length=50000)
    category: Optional[str] = None


class PostOut(BaseModel):
    title: str
    content: str
    category: Optional[str] = None
    created_at: datetime
