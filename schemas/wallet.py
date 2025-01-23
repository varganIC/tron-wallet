import datetime

from pydantic import BaseModel


class TronWalletInfo(BaseModel):
    address: str
    balance: float
    bandwidth: str
    energy: str


class WalletQueryBase(BaseModel):
    address: str


class WalletQueryCreate(WalletQueryBase):
    pass


class WalletQuery(WalletQueryBase):
    id: int
    date: datetime.datetime
