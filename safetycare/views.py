from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def safetycare(request):
    return render(request, "safetycare.html")