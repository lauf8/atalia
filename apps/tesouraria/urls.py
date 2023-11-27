from django.urls import path
from .views.views_create import (conta_create, entrada_create,fornecedor_create, 
                                tipo_entrada_create, tipo_saida_create )
from .views.views_list import (list_despesa, list_entradas, 
                               list_despesa_especific, list_entrada_especific, show_conta,
                               show_entrada)
urlpatterns = [
    path('despesa/create',conta_create, name='conta_create' ),
    path('despesa/',list_despesa, name='list_despesa'),
    path('despesa/<int:pk>',list_despesa_especific, name='list_despesa_especific'),
    path('despesa/<int:pk>/show',show_conta, name='show_conta'),
    
    path('entrada/create',entrada_create, name='entrada_create'),
    path('entrada',list_entradas, name='list_entrada' ),
    path('entrada/<int:pk>',list_entrada_especific, name='list_entrada_especific'),
    path('entrada/<int:pk>/show',show_entrada, name='show_entrada'),
    path('fornecedor/create',fornecedor_create, name='fornecedor_create' ),    
    path('tipo-entrada/create',tipo_entrada_create, name='tipo_entrada_create' ),  
    path('tipo-saida/create',tipo_saida_create, name='tipo_saida_create' ),    
]
