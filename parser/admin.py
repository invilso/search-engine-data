import site
from django.contrib import admin
from .models import Site, QueryesPool
# Register your models here.

admin.site.register(Site)
admin.site.register(QueryesPool)