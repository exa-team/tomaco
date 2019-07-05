import pytest

from tomaco import create_app


@pytest.fixture
def app():
    return create_app()
