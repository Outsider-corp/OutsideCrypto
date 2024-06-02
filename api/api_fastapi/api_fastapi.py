from fastapi import FastAPI
from api.api_fastapi.responses import MainJSONResponce
from api.api_fastapi.users.routers import get_routers

app = FastAPI(
    default_response_class=MainJSONResponce,
)

for router in get_routers():
    app.include_router(router=router.get('router'),
                       prefix=router.get('prefix'),
                       tags=['auth'])


# @app.on_event('startup')
# async def startup():
#     await database.connect()
#
# @app.on_event('shutdown')
# async def shutdown():
#     await database.disconnect


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
