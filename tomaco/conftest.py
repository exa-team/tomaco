import pytest
from webtest import TestApp

from tomaco.app import application


@pytest.fixture
def app():
    return TestApp(app=application)
