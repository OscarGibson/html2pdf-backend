try:
    from src.settings.local import *
except ImportError:
    raise Exception('Please create local.py file')
