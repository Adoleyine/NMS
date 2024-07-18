from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'base.html')

def scan_network(request):
    return render(request, 'scan/scan.html')