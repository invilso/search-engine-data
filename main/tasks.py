from celery import shared_task
from .services.create_excel import main as main_excel
from .services.create_json import main as main_json

@shared_task
def create_excel_task():  
    return main_excel()

@shared_task
def create_json_task():  
    return main_json()