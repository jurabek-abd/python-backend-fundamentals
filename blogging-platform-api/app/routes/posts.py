from dependencies import get_db
from fastapi import APIRouter, Depends, status
from models.post import Post
from schemas.post import PostCreate, PostOut
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=PostOut, status_code=status.HTTP_201_CREATED)
async def create_post(payload: PostCreate, db: Session = Depends(get_db)):
    """Create a new post."""

    new_post = Post(**payload.model_dump())

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post
