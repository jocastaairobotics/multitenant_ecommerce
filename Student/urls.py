from django.urls import path
from .views import StudentFormView, CreateStudentView, GetFormStudent, UpdateStudentView, deleteStudentView

urlpatterns = [
    path(route='index', view=StudentFormView, name="StudentFormView"),
    path(route='create', view=CreateStudentView, name="CreateStudentView"),
    path(route='get/<id>', view=GetFormStudent, name="GetFormStudent"),
    path(route='update/<id>', view=UpdateStudentView, name="UpdateStudentView"),
    path(route='delete/<id>', view=deleteStudentView, name="deleteStudentView"),
]
