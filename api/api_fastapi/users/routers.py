from typing import Dict, List

from fastapi import Depends
from fastapi_users import FastAPIUsers

from api.api_fastapi.users.auth.auth_backend import get_auth_backends
from database.users.adapters import get_user_adapter
from database.users.managers import get_user_manager_class
from database.users.schemas import UserCreate, User


async def get_user_manager(user_db=Depends(get_user_adapter)):
    um = get_user_manager_class()
    yield um(user_db)


fastapi_users_obj = FastAPIUsers(
    get_user_manager,
    get_auth_backends(),
)


def get_auth_routers() -> List[Dict]:
    routers = [{'prefix': f'/{auth_backend.name}',
                'router': fastapi_users_obj.get_auth_router(auth_backend)} for auth_backend in
               get_auth_backends()]
    return routers


def get_register_router() -> Dict:
    router = {'prefix': f'/auth',
              'router': fastapi_users_obj.get_register_router(User, UserCreate)}
    return router


def get_verify_router():
    router = {'prefix': f'/auth',
              'router': fastapi_users_obj.get_verify_router(User)}
    return router


def get_routers():
    return get_auth_routers() + [get_register_router(), get_verify_router()]
