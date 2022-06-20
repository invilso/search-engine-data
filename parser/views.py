from django.shortcuts import render
from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .tasks import create_queryes, start_parse
from django.http import HttpResponse
from .services.view_process import get_html
from .services.db import write_to_site_db, is_website_exist_in_db, get_any_query
import json

@method_decorator(csrf_exempt, name='dispatch')
class CreateView(ListView):
    def post(self, request):
        print(request.body)
        data = json.loads(request.body)
        task = create_queryes.delay(data)
        return JsonResponse({'status': f'success task runned id: {task.id}'})
    
@method_decorator(csrf_exempt, name='dispatch')
class StartView(ListView):
    def post(self, request):
        task = start_parse.delay()
        return JsonResponse({'status': f'success task runned id: {task.id}'})
    
class ProcessView(ListView):
    def get(self, request):
        return HttpResponse(get_html())
    
@method_decorator(csrf_exempt, name='dispatch')
class IsExistWebsiteView(ListView):
    def post(self, request):
        data = json.loads(request.body)
        return JsonResponse({'status': is_website_exist_in_db(data["website"])})
    
class GetQueryView(ListView):
    def get(self, request):
        return JsonResponse({'result': get_any_query()})
    
@method_decorator(csrf_exempt, name='dispatch')
class AddToDbView(ListView):
    def post(self, request):
        data = json.loads(request.body)
        return JsonResponse({'status': write_to_site_db(data)})
