from django.db import models

# Create your models here.
class Site(models.Model):
    organisation = models.CharField(max_length=250)
    thematic = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    website = models.URLField()
    state = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=70, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f"{self.id} - {self.email} - {self.organisation}"
    