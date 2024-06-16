from fastapi import FastAPI, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from api.api_fastapi.responses import MainJSONResponce
from api.api_fastapi.users.routers import get_auth_routers, get_register_router, get_verify_router
from database.database import engine
from database.users.adapters import get_async_session
from database.users.models import User

app = FastAPI(
    default_response_class=MainJSONResponce,
)

for router in get_auth_routers():
    app.include_router(router=router.get('router'),
                       prefix=router.get('prefix'),
                       tags=['auth'])

app.include_router(router=get_register_router().get('router'),
                   prefix=get_register_router().get('prefix'),
                   tags=['register'])

app.include_router(router=get_verify_router().get('router'),
                   prefix=get_verify_router().get('prefix'),
                   tags=['verify'])


@app.on_event('startup')
async def startup():
    await engine.connect()


#
@app.on_event('shutdown')
async def shutdown():
    await engine.disconnect()


@app.get('/')
def index():
    return {
        'code': 200
    }


@app.get('/test')
def test():
    return {
        'code': 400
    }


@app.get('/users')
async def get_users(session: AsyncSession = Depends(get_async_session)):
    async with session.begin():
        users = await session.execute(select(User))
        users = users.scalars().all()
        return {'users': users}
