from flask import Flask
from tomaco import wsgi


def test_should_create_a_flask_app():
    type(wsgi.application) == Flask
