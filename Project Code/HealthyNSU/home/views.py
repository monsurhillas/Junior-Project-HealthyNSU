from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html',{'title': 'Home'})

def about(request):
    return render(request, 'home/about.html',{'title' : 'About'})

def nearhospital(request):
    return render(request, 'home/nearhospital.html',{'title': 'Nearest Hospitals'})
# Create your views here.
