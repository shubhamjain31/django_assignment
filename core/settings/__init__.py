from .base import *
import os

if config("ENV_NAME") == 'production':
    from .production import *
else:
    from .development import *