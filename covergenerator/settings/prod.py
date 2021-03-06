from .common import *


STATICFILES_STORAGE = 'covergenerator.storages.StaticStorage'
DEFAULT_FILE_STORAGE = 'covergenerator.storages.MediaStorage'

AZURE_ACCOUNT_NAME = os.environ['AZURE_ACCOUNT_NAME']
AZURE_ACCOUNT_KEY = os.environ['AZURE_ACCOUNT_KEY']
AZURE_SSL = True