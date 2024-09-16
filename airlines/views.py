from django.shortcuts import render

# Create your views here.

def index(request):
    flights = Flight
    return render(request, "airlines/index.html")