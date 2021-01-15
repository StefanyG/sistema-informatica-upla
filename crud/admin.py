from django.contrib import admin
from .models import *

admin.site.register(Member)
#admin.site.register(Persona)
#admin.site.register(AreaDeDesarrollo)
#admin.site.register(HistorialAcademico)

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# admin.site.register(item)
@admin.register(Lista)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id_persona', )

@admin.register(Persona)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id_persona', )

@admin.register(AreaDeDesarrollo)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id_a_desarrollo', )

@admin.register(HistorialAcademico)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id_historial', )