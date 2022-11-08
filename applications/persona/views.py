from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)
# models
from .models import Empleado
# forms
from .forms import EmpleadoForm
# 1- lista todos los empleados de la empresa
# 2- listar todos los empleados que pertenecen a un area de la empresa
# 3- listar empleados por trabajo
# 4- listar los empleados por palabra clave
# 5- listar habilidades de un empleado

class InicioView(TemplateView):
    """ vista que carga la pagina de inicio"""
    template_name = 'inicio.html'


class ListAllEmpleado(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'empleado'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", "")
        lista = Empleado.objects.filter(
            first_name__icontains=palabra_clave
        )
        return lista


class ListByAreaEmpleado(ListView):
    """ Lista empleados de un area """
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        #El codigo que yo quiera
        area = self.kwargs["shorname"]
        lista = Empleado.objects.filter(
            departamento__shor_name=area
    )
        return lista 


class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleado'
    model = Empleado
    

class ListEmpleadoByJob(ListView):
    """ Lista empleados por trabajo """
    template_name = 'persona/list_by_job.html'

    def get_queryset(self):
        #El codigo que yo quiera
        area = self.kwargs["job"]
        lista = Empleado.objects.filter(
            job=area 
    )
        return lista 


class ListEmpleadosByKword(ListView):
    """ Lista empleados por palabra clave """
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print("********************")
        palabra_clave = self.request.GET.get("kword", "")
        lista = Empleado.objects.filter(
            first_name=palabra_clave
    )
        return lista


class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = "habilidades"

    def get_queryset(self):
        employee_id = self.request.GET.get("employee_id", 1)
        empleado = Empleado.objects.get(id=employee_id)
        return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        #todo un proceso
        context["titulo"] =  "Empleado del mes"
        return context


class SuccessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
        #logica del codigo/proceso
        empleado = form.save(commit=False)
        empleado.full_name = f"{empleado.first_name} {empleado.last_name}"
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.objects = self.get_object()
        print('**********METODO POST**********')
        print('====================')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        #logica del codigo/proceso
        print('**********METODO form valid**********')
        print('********************')
        return super(EmpleadoUpdateView, self).form_valid(form)
        
    
class EmpleadoDeleteView(DeleteView):
    template_name = "persona/delete.html"
    model = Empleado
    
    success_url = reverse_lazy('persona_app:empleados_admin')














