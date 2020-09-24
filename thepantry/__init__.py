# This makes celery available to all of Django
from .celery import app as celery_app

__all__ = ('celery_app',)