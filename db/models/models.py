from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    Text,
    text
)

from common.helpers import decorator
from db.models.common import Base


@decorator("_asdict")
class TronWalletQuery(Base):
    __tablename__ = 'tron_wallet_query'

    id = Column(Integer, primary_key=True, index=True)
    address = Column(Text, nullable=False, index=True)
    date = Column(
        DateTime(timezone=False),
        server_default=text("CURRENT_TIMESTAMP")
    )
