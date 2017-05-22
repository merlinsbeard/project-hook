import environ
from .base import *

env = environ.Env()
env.read_env('.env_dev')


DATABASES = {
    'default': env.db(),
}

INSTALLED_APPS = [
    'rest_framework',
    'hooker',
        ] + INSTALLED_APPS
