from django.shortcuts import render
from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .tasks import adding_task
from django.http import HttpResponse
from .services.view_process import get_html
import json

@method_decorator(csrf_exempt, name='dispatch')
class TestView(ListView):
    def post(self, request):
        print(request.body)
        data = json.loads(request.body)
        task = adding_task.delay(data)
        return JsonResponse({'status': f'success task runned id: {task.id}'})
    
class ProcessView(ListView):
    def get(self, request):
        return HttpResponse(get_html())
