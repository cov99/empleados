from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .forms import NewDepartamentForm
from applications.persona.models import Empleado
from .models import Departamento

# Create your views here.


class DepartamentListView(ListView):
    template_name = "departament/lista.html"
    model = Departamento
    context_object_name = 'departamentos'



class NewDepartamentView(FormView):
    template_name = 'departament/new_departament.html'
    form_class = NewDepartamentForm
    success_url = '/'

    def form_valid(self, form):
        print('*****estamos en el form valid*****')

        depa = Departamento.objects.create(
            name=form.cleaned_data['departamento'],
            shor_name=form.cleaned_data['shorname']
        )
        depa.save()
        
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name= nombre,
            last_name= apellido,
            job='1',
            departamento=depa
        )
        return super(NewDepartamentView, self).form_valid(form)
