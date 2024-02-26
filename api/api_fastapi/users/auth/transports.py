from fastapi_users.authentication import CookieTransport

import settings


def get_transport():
    return CookieTransport(cookie_max_age=settings.USER_AUTH_MAX_PAGE,
                           cookie_httponly=True,
                           cookie_secure=True)
