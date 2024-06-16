import uuid

from fastapi_users import schemas
from pydantic import Field

from settings import MIN_USERNAME_LENGTH


class User(schemas.BaseUser[uuid.UUID]):
    login: str = Field(min_length=MIN_USERNAME_LENGTH)


class UserCreate(schemas.BaseUserCreate):
    login: str = Field(min_length=MIN_USERNAME_LENGTH)


class UserUpdate(schemas.BaseUserUpdate):
    login: str = Field(min_length=MIN_USERNAME_LENGTH)
