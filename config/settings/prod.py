import environ
from .base import *

env = environ.Env()
env.read_env('prod.env')

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': env.db(),
}

INSTALLED_APPS = [
    'rest_framework',
    'hooker',
    'prompts',
        ] + INSTALLED_APPS

# Reddit secrets
REDDIT_SECRET = env("REDDIT_SECRET")
REDDIT_ID = env("REDDIT_ID")
REDDIT_USERNAME = env("REDDIT_USERNAME")
REDDIT_PASSWORD = env("REDDIT_PASSWORD")

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
