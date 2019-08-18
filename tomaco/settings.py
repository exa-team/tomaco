import os


class Config:
    DEBUG = False
    DEVELOPMENT = False
    TESTING = False

    SECRET_KEY = os.environ.get("SECRET_KEY", "should-be-a-secret-key")

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    # Auth
    GITHUB_CLIENT_ID = os.environ.get("GITHUB_CLIENT_ID", "should-be-client-id")
    GITHUB_CLIENT_SECRET = os.environ.get(
        "GITHUB_CLIENT_SECRET", "should-be-client-secret"
    )
    GITHUB_CALLBACK_URI = os.environ.get(
        "GITHUB_CALLBACK_URI", "http://localhost:8080/login/complete"
    )
    GITHUB_AUTHORIZE_URL = os.environ.get(
        "GITHUB_AUTHORIZE_URL", "https://github.com/login/oauth/authorize"
    )
    GITHUB_ACCESS_TOKEN_URL = os.environ.get(
        "GITHUB_ACCESS_TOKEN_URL", "https://github.com/login/oauth/access_token"
    )
    GITHUB_USER_RESOURCE_URL = os.environ.get(
        "GITHUB_USER_RESOURCE_URL", "https://api.github.com/user"
    )
    GITHUB_SCOPE = "email"


class Production(Config):
    pass


class Development(Config):
    DEBUG = True
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "postgresql://root@localhost/tomaco_dev")


class Testing(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite://"
