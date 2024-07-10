from pydantic import BaseModel


class WalletCreate(BaseModel):
    wallet_id: int
    user_id: int
    wallet_address: str
    wallet_name: str
    wallet_soft: bool
    blockchain_id: int
