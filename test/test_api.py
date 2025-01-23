from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient


def test_post_address(
    test_app: TestClient,
    address_wallet_data
):
    response = test_app.post(
        f'{pytest.api_prefix}/wallet',
        json=address_wallet_data
    )
    assert response.status_code == HTTPStatus.OK
    response_data = response.json()
    assert address_wallet_data['address'] == response_data['address']
