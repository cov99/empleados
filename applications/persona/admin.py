from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.
admin.site.register(Habilidades)


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "job",
        "departamento",
        "full_name",
        "id",
    )
    #
    def full_name(self, obj):
        #toda la operacion
        print(obj.first_name)
        return f"{obj.first_name} {obj.last_name}"
        #texto formateado  con definicion de tipos:
        #return "%s %s".format(obj.first_name, obj.last_name) 

        #return obj.first_name + ' ' + obj.last_name NO HACER
    #
    search_fields = ("first_name",)
    list_filter = ("departamento", "job", "habilidades",)
    #
    filter_horizontal = ("habilidades",)
admin.site.register(Empleado, EmpleadoAdmin)