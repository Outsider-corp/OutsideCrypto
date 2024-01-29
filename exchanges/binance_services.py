import os
import asyncio
import websockets
from dotenv import load_dotenv
from binance import AsyncClient

load_dotenv()


async def get_account_coins():
    client = AsyncClient(api_key=os.environ.get('BINANCE_API_PUBLIC'),
                         api_secret=os.environ.get('BINANCE_API_SECRET'))
    coins = await client.get_account()
    coins = [coin for coin in coins['balances'] if float(coin['free'])]
    await client.close_connection()


async def get_price():
    pass


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_account_coins())
