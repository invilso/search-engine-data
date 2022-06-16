from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .tasks import create_excel_task, create_json_task
from .services.create_excel import main as create_excel
from .services.create_json import main as create_json
import io
from django.http import FileResponse


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
    
    
class DownloadXLSX(ListView):
    def get(self, request):
        return FileResponse(open(create_excel(),'rb')) 
    
class DownloadJSON(ListView):
    def get(self, request):
        return FileResponse(open(create_json(),'rb')) 
    
    
class MainView(ListView):
    def get(self, request):
        return render(request=request, template_name='main/main.html')
    
    
# Create your views here.
