from django.shortcuts import render

def home(request):     
    return render(request, 'pages/home.html')

def tarot(request):
    return render(request, 'pages/tarot.html')

def pyros(request):
    return render(request, 'pages/pyros.html')

def features(request): 
    return render(request, 'pages/features.html')

def faq(request):
    return render(request, 'pages/faq.html')