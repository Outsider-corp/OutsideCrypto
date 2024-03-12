from fastapi import Depends
from fastapi_users import FastAPIUsers

from api.api_fastapi.users.auth.auth_backend import get_auth_backends
from database.users.adapters import get_user_adapter
from database.users.managers import get_user_manager_class


async def get_user_manager(user_db=Depends(get_user_adapter)):
    um = get_user_manager_class()
    yield um(user_db)

fastapi_user = FastAPIUsers(
    get_user_manager,
    get_auth_backends(),

)