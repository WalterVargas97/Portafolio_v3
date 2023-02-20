from django.shortcuts import render
from .models import Project
from .models import Experience
# Create your views here.

def mainView(request):
    project = Project.objects.all()
    experience = Experience.objects.all()
    return render(request, 'home.html', {'project':Project, 'experience':Experience})
