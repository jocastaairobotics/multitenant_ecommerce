from django.shortcuts import render
from django.views.generic import FormView, CreateView
from .forms import AccountForm
from .models import Account
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class AccountFormView(FormView):
    form_class = AccountForm
    template_name = "banking/create.html"


class AccountCreateView(CreateView):
    model = Account
    fields = "__all__"
    success_url = "/banking/form"


class AccountListView(ListView):
    model = Account
    template_name = "banking/index.html"


class AccountDetailView(DetailView):
    model = Account
