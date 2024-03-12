import re
import uuid
from typing import Union, Optional

from fastapi_users import BaseUserManager, UUIDIDMixin, schemas, models, InvalidPasswordException
from starlette.requests import Request

import settings
from database.users.models import User


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = settings.USER_RESET_PASSWORD_TOKEN_SECRET
    verification_token_secret = settings.USER_VERIFICATION_TOKEN_SECRET

    async def validate_password(
            self, password: str, user: Union[schemas.UC, models.UP]
    ) -> None:
        if len(password) < 8:
            raise InvalidPasswordException(reason=f'Password should be at least 8 characters')
        if not (re.search(r'\d', password) and
                re.search(r'[A-Z]', password) and
                re.search(r'[a-z]', password)):
            raise InvalidPasswordException(
                reason=f'Password should contain number, uppercase and lowercase characters')

    async def on_after_register(
            self, user: models.UP, request: Optional[Request] = None
    ) -> None:
        print(f'User {user.id} has registered.')


def get_user_manager_class():
    return UserManager
