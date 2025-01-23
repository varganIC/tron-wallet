from typing import List, Optional

from fastapi import (
    APIRouter,
    Body,
    Depends,
    HTTPException,
    Query,
    status
)
from sqlalchemy.ext.asyncio import AsyncSession

import api_routes.metadata as meta
from api_routes.common import (
    BaseResponse,
    responses_common_200_desc,
    responses_common_get,
    responses_common_post
)
from db import crud, database
from schemas.wallet import (
    TronWalletInfo,
    WalletQuery,
    WalletQueryCreate
)
from services.tron.tron_service import TronAccountService, get_tron_client

router = APIRouter(prefix=meta.api_prefix)
TAG = 'Кошелек'


@router.post(
    "/wallet",
    tags=[TAG],
    summary="Поулчить информацию о кошельке",
    response_model=TronWalletInfo,
    responses=responses_common_post,
    response_description=responses_common_200_desc
)
async def get_wallet_info(
    item: WalletQueryCreate = Body(...),
    service_tron: TronAccountService = Depends(get_tron_client),
    db: AsyncSession = Depends(database.get_db_async)
):
    wallet_info = service_tron.get_account_info(item.address)

    if 'error' in wallet_info:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'{wallet_info.get("error")}',
        )

    result = TronWalletInfo(**wallet_info)
    await crud.create_tron_query(db, item)

    return result


@router.get(
    "/wallet/history",
    tags=[TAG],
    summary="История запросов к кошелькам",
    response_model=List[WalletQuery],
    responses=responses_common_get,
    response_description=responses_common_200_desc
)
async def get_wallet_history(
    take:  Optional[int] = Query(None),
    skip: Optional[int] = Query(None),
    db: AsyncSession = Depends(database.get_db_async)
):
    return BaseResponse(WalletQuery).get_typed_response_multi_as_model(
        await crud.get_wallet_history(db, take, skip)
    )
