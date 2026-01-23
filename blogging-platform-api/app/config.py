from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Blogging Platform API"
    app_version: str = "0.1.0"
    app_description: str = "Blogging Platform API built with FastAPI"
    debug: bool = True
    database_url: str = ""

    class Config:
        env_file = ".env"


settings = Settings()
