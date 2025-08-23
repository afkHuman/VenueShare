from django.http import HttpResponse
from django.template import loader
from .models import Venues
from django.shortcuts import get_object_or_404, render


# Create your views here.
def venues(request):
    return render(request, 'main.html')