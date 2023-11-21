from django.urls import path
from .views import AccountFormView, AccountCreateView, AccountListView, AccountDetailView, AccountUpdateView

urlpatterns = [
    path("form", AccountFormView.as_view(), name="AccountFormView"),
    path("create", AccountCreateView.as_view(), name="AccountCreateView"),
    path("list", AccountListView.as_view(), name="AccountListView"),
    path("<pk>/detail", AccountDetailView.as_view(), name="AccountDetailView"),
    path("<pk>/update", AccountUpdateView.as_view(), name="AccountUpdateView"),
]