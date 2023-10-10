from django.http import HttpResponse
from django.shortcuts import render


def Home(request):
    return render(request=request, template_name='index.html', context=None)


def About(request):
    return render(request=request, template_name='about.html', context=None)


def Privacy(request):
    return render(request=request, template_name='privacy.html', context=None)


def Career(request):
    return render(request=request, template_name='career.html', context=None)
