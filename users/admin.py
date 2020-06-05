from django.contrib import admin
from .models import Resultado


class ResultadoAdmin(admin.ModelAdmin):
    list_display = ('perspicuidad', 'user')
    list_filter = ('user','perspicuidad')

admin.site.register(Resultado,ResultadoAdmin)
