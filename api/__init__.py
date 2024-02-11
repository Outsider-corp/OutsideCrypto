from hypercorn import Config
from hypercorn.asyncio import serve

from api.api_fastapi.api_fastapi import app


async def run_api():
    await serve(app, Config())
