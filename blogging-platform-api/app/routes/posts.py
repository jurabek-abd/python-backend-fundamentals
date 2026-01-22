from dependencies import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from models.post import Post
from schemas.post import PostCreate, PostOut, PostUpdate
from sqlalchemy import or_
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=list[PostOut])
async def get_posts(term: str = "", db: Session = Depends(get_db)):
    """Get posts. Optional filtering by term."""

    posts = (
        db.query(Post)
        .filter(
            or_(
                Post.title.ilike(f"%{term}%"),
                Post.category.ilike(f"%{term}%"),
                Post.content.ilike(f"%{term}%"),
            )
        )
        .all()
    )

    return posts


@router.post("/", response_model=PostOut, status_code=status.HTTP_201_CREATED)
async def create_post(payload: PostCreate, db: Session = Depends(get_db)):
    """Create a new post."""

    new_post = Post(**payload.model_dump())

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


@router.get("/{post_id}", response_model=PostOut)
async def get_post_by_id(post_id: str, db: Session = Depends(get_db)):
    """Get a specific post by ID."""

    post = db.get(Post, post_id)

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )

    return post


@router.put("/{post_id}", response_model=PostOut)
async def update_post_by_id(
    post_id: str, payload: PostUpdate, db: Session = Depends(get_db)
):
    """Update a specific post by ID."""

    try:
        post = db.get(Post, post_id)

        if post is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
            )

        if payload.title is not None:
            post.title = payload.title
        if payload.content is not None:
            post.content = payload.content
        if payload.category is not None:
            post.category = payload.category
        if payload.tags is not None:
            post.tags = payload.tags

        db.commit()
        return post
    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update a post",
        )


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post_by_id(post_id: str, db: Session = Depends(get_db)):
    """Delete a specific post by ID."""

    post = db.get(Post, post_id)

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )

    db.delete(post)
    db.commit()
    return
