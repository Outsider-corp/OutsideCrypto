from fastapi_users import schemas
from pydantic import Field

from settings import MIN_USERNAME_LENGTH


class User(schemas.BaseUser):
    username: str = Field(min_length=MIN_USERNAME_LENGTH)


class UserCreate(schemas.BaseUserCreate):
    username: str = Field(min_length=MIN_USERNAME_LENGTH)


class UserUpdate(schemas.BaseUserUpdate):
    username: str = Field(min_length=MIN_USERNAME_LENGTH)
