import os

SECRET_KEY = os.environ.get("SECRET_KEY", "should-be-a-secret-key")

# Auth
GITHUB_CLIENT_ID = os.environ.get("GITHUB_CLIENT_ID", "should-be-client-id")
GITHUB_CLIENT_SECRET = os.environ.get("GITHUB_CLIENT_SECRET", "should-be-client-secret")
GITHUB_CALLBACK_URI = os.environ.get(
    "GITHUB_CALLBACK_URI", "http://localhost:8080/login/complete"
)
GITHUB_AUTHORIZE_URL = "https://github.com/login/oauth/authorize"
GITHUB_ACCESS_TOKEN_URL = "https://github.com/login/oauth/access_token"
GITHUB_USER_RESOURCE_URL = "https://api.github.com/user"
GITHUB_SCOPE = "email"
