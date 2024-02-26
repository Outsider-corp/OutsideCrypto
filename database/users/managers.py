import uuid

from fastapi import Depends
from fastapi_users import BaseUserManager, UUIDIDMixin

import settings
from database.users.adapters import get_user_db
from database.users.models import User
from database.users.schemas import UserCreate


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = settings.USER_RESET_PASSWORD_TOKEN_SECRET
    verification_token_secret = settings.USER_VERIFICATION_TOKEN_SECRET


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
