from django.urls import path
from . import views

app_name = 'parser'

urlpatterns = [
    path('start-parse/', views.TestView.as_view(), name='start'),
    path('view-process/', views.ProcessView.as_view(), name='view_process'),
]