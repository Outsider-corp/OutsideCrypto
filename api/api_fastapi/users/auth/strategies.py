from fastapi_users.authentication import JWTStrategy

import settings


def get_jwt_strategy():
    return JWTStrategy(secret=settings.USER_TOKEN_SECRET,
                       lifetime_seconds=settings.USER_AUTH_MAX_PAGE)
