from fastapi import APIRouter, Depends
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
async def get_user_wallets(user_id: int,
                           session: AsyncSession = Depends(get_async_session)):
    query = select(Wallet).where(Wallet.user_id == user_id)
    result = await session.execute(query)
    return result.scalars().all()


@router.post('/add_wallet')
async def add_wallet(new_wallet: WalletCreate,
                     session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Wallet).values(**new_wallet.dict())
    await session.execute(stmt)
    await session.commit()
    return {'status': 'success'}
