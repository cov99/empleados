from django.contrib import admin
from django.urls import path
from . import views

app_name = "departamento_app"

urlpatterns = [
    path(
        'departament-list/',
     views.DepartamentListView.as_view(),
      name='departament_list'),
    path(
        'new-departament/',
        views.NewDepartamentView.as_view(),
        name='new_departament'
        ),
]

