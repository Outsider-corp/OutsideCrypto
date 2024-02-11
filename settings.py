import os

from dotenv import load_dotenv

load_dotenv()

API_VERSION = os.environ.get('API_VERSION')

DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
COOKIE_SECRET = os.environ.get('COOKIE_SECRET')
AUTH_SECRET = os.environ.get('AUTH_SECRET')


DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


MIN_USERNAME_LENGTH = 5
