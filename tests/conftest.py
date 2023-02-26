import pytest

from src.app import app


@pytest.fixture(scope="session")
def client():
    with app.test_client() as client:
        with app.app_context():
            yield client
