from django.shortcuts import render
from django.http import HttpResponse


def productHome(request, name):
    ctx = {
        "name": name
    }
    return render(request, template_name='products/index.html', context=ctx)
