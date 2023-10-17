"""
URL configuration for multitenant_ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from .views import Home, About, Privacy, Career

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(route="home", view=Home, name="Home"),
    path(route="about", view=About, name="About"),
    path(route="api/privacy", view=Privacy, name="Privacy"),
    path(route="api/career", view=Career, name="Career"),
    path('product/', include("Products.urls"))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
