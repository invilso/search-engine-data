import os  
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'search_engine_data.settings')
celery_app = Celery('search_engine_data')  
celery_app.config_from_object('django.conf:settings', namespace='CELERY')  
celery_app.autodiscover_tasks() 