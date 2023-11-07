from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductForm
from .models import Product


def productHome(request):
    form = ProductForm()
    p = Product.objects.all()
    ctx = {
        "form": form,
        "product": p
    }
    return render(request, template_name='products/index.html', context=ctx)


def createProduct(request):
    data = request.POST
    name = data.get("kanif")
    description = data.get("santoshi")
    price = data.get("niraj")
    rating = data.get("pratik")

    p = Product(name=name, description=description, price=price, rating=rating)
    p.save()

    return redirect("/product/index")
