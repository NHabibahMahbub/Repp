from django.shortcuts import render
from .models import Platform


def home(request):
    platforms = Platform.objects.all()
    return render(request, 'home.html', {'platforms': platforms})
