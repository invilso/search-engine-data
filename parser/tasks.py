from celery import shared_task
from .services.task import main

@shared_task
def adding_task(x, y):  
    main()