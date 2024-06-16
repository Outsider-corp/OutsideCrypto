from typing import Iterable, Sequence

from fastapi_users.authentication import AuthenticationBackend

from api.api_fastapi.users.auth.strategies import get_jwt_strategy
from api.api_fastapi.users.auth.transports import get_transport

auth_jwt_backend = AuthenticationBackend(name='auth_backend',
                                         transport=get_transport(),
                                         get_strategy=get_jwt_strategy)


def get_auth_backends() -> Sequence[AuthenticationBackend]:
    return [auth_jwt_backend]
