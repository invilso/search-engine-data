from celery import shared_task
from .services.create_queryes import main
from .services.task import main as start

@shared_task
def create_queryes(data: dict):  
    mode = 0
    ignore = True
    if data['mode'] == 'city':
        mode = 1
        if data.get('ignore'):
            ignore = data.get('ignore')
    elif data['mode'] == 'state':
        mode = 2
    else:
        mode = 0
    return main(data['queryes'], mode, ignore)

@shared_task
def start_parse():  
    return start()