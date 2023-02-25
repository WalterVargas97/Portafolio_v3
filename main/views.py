from django.shortcuts import render, get_object_or_404
from .models import project


# Create your views here.

def main(request):
    projects = project.objects.all()
    return render(request, 'home.html', {'projects':projects} )
