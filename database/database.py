from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeMeta, sessionmaker

from settings import DATABASE_URL


engine = create_engine(DATABASE_URL)
Base: DeclarativeMeta = declarative_base()
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
