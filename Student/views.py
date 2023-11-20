from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
from django.views.generic.list import ListView


def StudentFormView(request):
    form = StudentForm()
    data = Student.objects.all()
    ctx = {
        "form": form,
        "data": data
    }
    return render(request=request, template_name="student/index.html", context=ctx)


def CreateStudentView(request):
    data = request.POST
    print(data)
    form = StudentForm(data=data)
    if form.is_valid():
        form.save()
    else:
        ctx = {
            "form": form
        }
        return render(request=request, template_name="student/index.html", context=ctx)
    return redirect("/student/index")


def GetFormStudent(request, id):
    data = Student.objects.get(id=id)
    form = StudentForm(instance=data)
    ctx = {
        "form": form,
        "id": data.id
    }
    return render(request=request, template_name="student/update.html", context=ctx)


def UpdateStudentView(request, id):
    st = Student.objects.get(id=id)
    data = request.POST
    form = StudentForm(instance=st, data=data)
    if form.is_valid():
        form.save()
    else:
        ctx = {
            "form": form
        }
        return render(request=request, template_name="student/update.html", context=ctx)
    return redirect("/student/index")


def deleteStudentView(request, id):
    st = Student.objects.get(id=id)
    st.delete()
    return redirect("/student/index")

