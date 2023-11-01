from django.urls import path
from .views import productHome, createProduct

urlpatterns = [
    path(route='index', view=productHome, name="Product"),
    path(route="create", view=createProduct, name="CreateProduct")
]
