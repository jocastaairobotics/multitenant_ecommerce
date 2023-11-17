from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from django.views import View


class EmployeeView(View):

    def get(self, request):
        form = EmployeeForm()
        data = Employee.objects.all()
        ctx = {
            "form": form,
            "data": data
        }
        return render(request=request, template_name="employee/index.html", context=ctx)

    def post(self, request):
        data = request.POST
        print(data)
        form = EmployeeForm(data=data)
        if form.is_valid():
            form.save()
        else:
            ctx = {
                "form": form
            }
            return render(request=request, template_name="employee/index.html", context=ctx)
        return redirect("/employee/index")


class EmployeeUpdateView(View):

    def get(self, request, id):
        data = Employee.objects.get(id=id)
        form = EmployeeForm(instance=data)
        ctx = {
            "form": form,
            "id": data.id
        }
        return render(request=request, template_name="employee/update.html", context=ctx)

    def post(self, request, id):
        st = Employee.objects.get(id=id)
        data = request.POST
        form = EmployeeForm(instance=st, data=data)
        if form.is_valid():
            form.save()
        else:
            ctx = {
                "form": form
            }
            return render(request=request, template_name="employee/update.html", context=ctx)
        return redirect("/employee/index")
