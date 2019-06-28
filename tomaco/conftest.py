import pytest
from webtest import TestApp

from tomaco.app import app as application


@pytest.fixture
def app():
    return TestApp(app=application)
