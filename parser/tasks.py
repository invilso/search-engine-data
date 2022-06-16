from celery import shared_task
from .services.task import main

@shared_task
def adding_task(data: dict):  
    mode = 0
    if data['mode'] == 'city':
        mode = 1
    elif data['mode'] == 'state':
        mode = 2
    else:
        mode = 0
    return main(data['queryes'], mode)