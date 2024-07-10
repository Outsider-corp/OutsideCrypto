from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Integer, Column, String, DateTime
from sqlalchemy.orm import relationship

from database.database import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String, unique=True, nullable=False)
    hased_password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)

    wallet = relationship('Wallet', back_populates='user')




