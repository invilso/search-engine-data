from django.db import models

# Create your models here.
class Site(models.Model):
    name_contact_person = models.TextField(max_length=250, blank=True, null=True)
    organisation = models.TextField(max_length=250, blank=True, null=True)
    themes = models.TextField(max_length=250, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(unique=True, blank=True, null=True)
    url = models.URLField(unique=True)
    state = models.TextField(max_length=50, blank=True, null=True)
    city = models.TextField(max_length=50, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.text
    