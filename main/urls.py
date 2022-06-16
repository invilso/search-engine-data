from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('create-excel/', views.CreateExcel.as_view(), name='create_excel'),
    path('create-json/', views.CreateJson.as_view(), name='create_json'),
    path('download-excel/', views.DownloadXLSX.as_view(), name='download_excel'),
    path('download-json/', views.DownloadJSON.as_view(), name='download_json'),
    path('', views.MainView.as_view(), name='main'),
]