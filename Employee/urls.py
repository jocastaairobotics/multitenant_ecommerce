from django.urls import path
from .views import EmployeeView, EmployeeUpdateView

urlpatterns = [
    path(route="index", view=EmployeeView.as_view(), name="Employee"),
    path(route="update/<id>", view=EmployeeUpdateView.as_view(), name="EmployeeUpdateView")
]
