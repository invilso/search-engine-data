from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .tasks import create_excel_task, create_json_task


@method_decorator(csrf_exempt, name='dispatch')
class CreateExcel(ListView):
    def get(self, request):
        task = create_excel_task.delay()
        return JsonResponse({'status': f'excel start create {task.id}'})
    
@method_decorator(csrf_exempt, name='dispatch')
class CreateJson(ListView):
    def get(self, request):
        task = create_json_task.delay()
        return JsonResponse({'status': f'excel start create {task.id}'})
    
    
class MainView(ListView):
    def get(self, request):
        return render(request=request, template_name='main/main.html')
    
    
# Create your views here.
