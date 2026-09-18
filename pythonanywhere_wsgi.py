import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

os.environ.setdefault('APP_ENV', 'production')
os.environ.setdefault('FLASK_DEBUG', '0')
os.environ.setdefault('SESSION_COOKIE_SECURE', '0')

from app import app as application
