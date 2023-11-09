from django.urls import path
from .views import productHome, createProduct, filterProduct, getProductDetailView

urlpatterns = [
    path(route='index', view=productHome, name="Product"),
    path(route="create", view=createProduct, name="CreateProduct"),
    path(route="filter", view=filterProduct, name="FilterProduct"),
    path(route="get_product/<id>", view=getProductDetailView, name="GetProductDetailView")
]
