from django.shortcuts import render
from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .tasks import adding_task

@method_decorator(csrf_exempt, name='dispatch')
class TestView(ListView):
    def get(self, request):
        task = adding_task.delay()
        return JsonResponse({'status': f'success task runned id: {task.id}'})
# Create your views here.
