from django.contrib import admin
from .models import Entidade, Membro, Patrimonio

admin.site.register(Entidade)
admin.site.register(Membro)
admin.site.register(Patrimonio)
