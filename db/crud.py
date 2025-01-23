from typing import List, Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from db.models.models import TronWalletQuery
from schemas.wallet import WalletQueryCreate


async def create_tron_query(
    db: AsyncSession,
    item: WalletQueryCreate
) -> TronWalletQuery:
    db_object = TronWalletQuery(**item.dict())
    db.add(db_object)
    await db.commit()

    return db_object


async def get_wallet_history(
    db: AsyncSession,
    take: Optional[int] = None,
    skip: Optional[int] = None
) -> List[TronWalletQuery]:
    return (
        await db.execute(
            select(TronWalletQuery)
            .order_by(TronWalletQuery.date.desc())
            .offset(skip)
            .limit(take)

        )
    ).scalars().all()
