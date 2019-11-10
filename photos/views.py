from django.shortcuts import render
from .models import Image

# Create your views here.
def locations(request):
    return render(request, 'photos/locations.html')


def index(request):
    images = Image.objects
    return render(request, 'photos/index.html', {'images':images})
