from django.urls import path
from . import views

app_name = 'parser'

urlpatterns = [
    path('create/', views.CreateView.as_view(), name='create'),
    path('start/', views.StartView.as_view(), name='start'),
    path('is-website-exist/', views.IsExistWebsiteView.as_view(), name='is_website_exist'),
    path('get-any-query/', views.GetQueryView.as_view(), name='get_any_query'),
    path('add-to-db/', views.AddToDbView.as_view(), name='add_to_db'),
    path('view-process/', views.ProcessView.as_view(), name='view_process'),
]