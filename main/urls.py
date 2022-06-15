from django.urls import path
from . import views

urlpatterns = [
    path('create-excel/', views.CreateExcel.as_view(), name='create_excel'),
    path('create-json/', views.CreateJson.as_view(), name='create_json'),
    path('', views.MainView.as_view(), name='main'),
]