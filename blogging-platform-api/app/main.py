from config import settings
from database.db import Base, engine
from fastapi import FastAPI
from routes.posts import router as posts_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=settings.app_description,
)
app.include_router(posts_router, prefix="/api/v1/posts", tags=["posts"])
