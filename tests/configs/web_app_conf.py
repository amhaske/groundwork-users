import os

APP_NAME = "test_web_app"
APP_DESCRIPTION = "web_app for user tests"
APP_LOGO = ""

APP_PATH = os.path.dirname(__file__)

PLUGINS = []

USERS_DB_URL = "sqlite:///"

FLASK_SECURITY_PASSWORD_SALT = "123"
# FLASK_SECURITY_PASSWORD_HASH = "bcrypt"
