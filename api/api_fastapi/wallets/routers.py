import time

from fastapi import APIRouter, Depends, HTTPException
from fastapi_cache.decorator import cache
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database.bank.models import Wallet
from database.bank.schemas import WalletCreate
from database.database import get_async_session

router = APIRouter(
    prefix='/wallet',
    tags=['Wallet'],
)


def get_wallet_router():
    return router



@router.get('/get_user_wallets')
@cache(expire=30)
async def get_user_wallets(user_id: int,
                           session: AsyncSession = Depends(get_async_session)):
    try:
        time.sleep(4)
        query = select(Wallet).where(Wallet.user_id == user_id)
        result = await session.execute(query)
        return {'status': 'success',
                'data': result.scalars().all()}
    except:
        raise HTTPException(status_code=500, detail={'status': 'error',
                                                     'data': None})


@router.post('/add_wallet')
async def add_wallet(new_wallet: WalletCreate,
                     session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Wallet).values(**new_wallet.dict())
    await session.execute(stmt)
    await session.commit()
    return {'status': 'success'}
