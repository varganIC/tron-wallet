from unittest.mock import AsyncMock

import pytest

from db import crud
from schemas.wallet import WalletQueryCreate


@pytest.mark.asyncio
async def test_save_address(address_wallet_data):
    mock_db = AsyncMock()

    wallet = await crud.create_tron_query(
        mock_db,
        WalletQueryCreate(
            address=address_wallet_data['address']
        )
    )

    mock_db.add.assert_called_once_with(wallet)
    mock_db.commit.assert_called_once()

    assert wallet.address == address_wallet_data['address']
