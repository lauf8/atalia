from django.contrib import admin
from .models import Tipo_arrecadacao, Tipo_conta, Contas, Arrecadacao, Fornecedor

admin.site.register(Tipo_arrecadacao)
admin.site.register(Tipo_conta)
admin.site.register(Contas)
admin.site.register(Arrecadacao)
admin.site.register(Fornecedor)
