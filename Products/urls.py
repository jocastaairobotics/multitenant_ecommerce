from django.urls import path
from .views import productHome

urlpatterns = [
    path(route='index/<str:name>', view=productHome, name="Product")
]
