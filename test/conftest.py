import pytest
from fastapi.testclient import TestClient

from api_routes.metadata import api_prefix
from app.main import app


def pytest_configure():
    pytest.api_prefix = api_prefix


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client


@pytest.fixture(scope="module")
def address_wallet_data():
    return {
        'address': 'TE2RzoSV3wFK99w6J9UnnZ4vLfXYoxvRwP'
    }
