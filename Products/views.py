from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductForm


def productHome(request):
    form = ProductForm()
    ctx = {
        "form": form
    }
    return render(request, template_name='products/index.html', context=ctx)


def createProduct(request):
    data = request.POST
    name = data.get("name")
    description = data.get("description")
    price = data.get("price")
    rating = data.get("rating")
    print(data)
    return redirect("/product/index")
