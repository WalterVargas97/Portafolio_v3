from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField



# Create your models here.
class project(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = ImageField(upload_to='portfolio/images/')
    url = URLField(blank=True)
    
class experience(models.Model):
    cargo =  models.CharField(max_length=200)
    empresa = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

