from typing import AsyncGenerator

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, \
    AsyncSession
from sqlalchemy.orm import declarative_base

from settings import DATABASE_URL

metadata = MetaData(schema='crypto')
Base = declarative_base(metadata=metadata)

engine = create_async_engine(DATABASE_URL)

async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
