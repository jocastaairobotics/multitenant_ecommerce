from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductForm, ProductFilterForm
from .models import Product


def productHome(request):
    form = ProductForm()
    filter = ProductFilterForm() #filter form
    p = Product.objects.all()
    ctx = {
        "form": form,
        "filter": filter,
        "product": p
    }
    return render(request, template_name='products/index.html', context=ctx)


def createProduct(request):
    data = request.POST
    name = data.get("name")
    description = data.get("description")
    price = data.get("price")
    rating = data.get("rating")

    p = Product(name=name, description=description, price=price, rating=rating)
    p.save()

    return redirect("/product/index")


def filterProduct(request):
    data = request.GET
    name = data.get("name")
    price = data.get("price")
    form = ProductForm()
    filter = ProductFilterForm()
    p = Product.objects.filter(name=name, price=price)
    ctx = {
        "form": form,
        "filter": filter,
        "product": p
    }
    return render(request, template_name='products/index.html', context=ctx)


def getProductDetailView(request, id):
    p = Product.objects.get(id=id)
    ctx = {
        "name":p.name,
        "description": p.description,
        "price": p.price,
        "rating": p.rating
    }
    return render(request, template_name='products/productDetail.html', context=ctx)
