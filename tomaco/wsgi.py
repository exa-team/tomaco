import os
from . import create_app

application = create_app(os.environ.get("APP_SETTINGS", "tomaco.settings.Development"))
