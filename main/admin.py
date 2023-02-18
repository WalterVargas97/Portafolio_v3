from django.contrib import admin
from .models import project
from .models import experience

# Register your models here.

admin.site.register(project)
admin.site.register(experience)