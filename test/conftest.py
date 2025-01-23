
import pytest
from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.testclient import TestClient

from api_routes.metadata import api_prefix
from app.main import app


def pytest_configure():
    pytest.api_prefix = api_prefix
    pytest.history_id = api_prefix


def remove_middleware(app: FastAPI, target: str) -> FastAPI:
    new_middlewares: list[Middleware] = []
    for middleware in app.user_middleware:
        if not middleware.cls.__name__ == target:
            new_middlewares.append(middleware)
    app.user_middleware = new_middlewares
    app.middleware_stack = app.build_middleware_stack()
    return app


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    remove_middleware(app, 'BaseHTTPMiddleware')
    yield client


@pytest.fixture(scope="module")
def address_wallet_data():
    return {
        'address': 'TE2RzoSV3wFK99w6J9UnnZ4vLfXYoxvRwP'
    }
