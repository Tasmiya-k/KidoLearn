from django.shortcuts import render, HttpResponse


def welcome(request):
    return render(request, 'Welcome2.html')

def language(request):
    return render(request, 'index.html')

def options(request):
    return render(request, 'options.html')

def language(request):
    return render(request, 'language.html')

def levelVege(request):
    return render(request, 'levels.html')

def levelVege1(request):
    return render(request, 'gamearea.html')

def levelVege2(request):
    return render(request, 'veglev2.html')