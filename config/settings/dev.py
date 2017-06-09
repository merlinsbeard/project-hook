import environ
from .base import *

env = environ.Env()
env.read_env('.env_dev')

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': env.db(),
}

INSTALLED_APPS = [
    'rest_framework',
    'hooker',
    'prompts',
        ] + INSTALLED_APPS
