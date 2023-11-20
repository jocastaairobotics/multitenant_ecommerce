from django.urls import path
from .views import AccountFormView, AccountCreateView, AccountListView

urlpatterns = [
    path("form", AccountFormView.as_view(), name="AccountFormView"),
    path("create", AccountCreateView.as_view(), name="AccountCreateView"),
    path("list", AccountListView.as_view(), name="AccountListView"),
]