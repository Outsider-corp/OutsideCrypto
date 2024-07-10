from sqlalchemy import Column, Integer, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship

from database.database import Base


class Wallet(Base):
    __tablename__ = 'wallet'

    wallet_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.user_id'), index=True)
    wallet_address = Column(String, nullable=False)
    wallet_name = Column(String, nullable=False)
    wallet_soft = Column(Boolean, default=True)
    blockchain_id = Column(Integer, ForeignKey('blockchain.blockchain_id'))

    user = relationship('User', back_populates='wallet')
    blockchain = relationship('Blockchain', back_populates='wallet')


class Blockchain(Base):
    __tablename__ = 'blockchain'

    blockchain_id = Column(Integer, primary_key=True, autoincrement=True)
    blockchain_name = Column(String, nullable=False)
    blockchain_coin = Column(String)

    wallet = relationship('Wallet', back_populates='blockchain')
