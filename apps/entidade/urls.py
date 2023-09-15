from django.urls import path
from .views.views_create import (create_marcon, clube_fraternidade_create, demolay_create, escudeiro_create,
                    fdj_create, abelinha_create, patrimonio_create, create_member)
from .views.views_list import (list_everthing, list_patrimonio, list_patrimonio_especifc, 
                               list_entidade_especific, list_members, list_members_especific)

urlpatterns = [
    
    path('',list_everthing, name='list_everthing' ),
    path('<int:pk>',list_entidade_especific, name='list_entidade_especific'),
    path('membros',list_members, name='list_members'),
    path('membros/<int:pk>',list_members_especific, name='list_members_especific'),
    path('membros/create',create_member, name='create_member'),
    

    

    #marcon
    path('marcon/create',create_marcon, name='create_marcon' ),
    
    #fraternidade
    path('clube/create',clube_fraternidade_create, name='clube_fraternidade_create' ),
    
    #demolay
    path('demolay/create',demolay_create, name='demolay_create'),
    
    #escudeiro
    path('escudeiro/create',escudeiro_create, name='escudeiro_create'),
    
     #fdj
    path('fdj/create',fdj_create, name='fdj_create'),
    
     #abelinha
    path('abelinha/create',abelinha_create, name='abelinha_create'),
    
    #patrimonio
    path('patrimonio/create',patrimonio_create, name='patrimonio_create'),
    path('patrimonio',list_patrimonio, name='list_patrimonio'),
    path('patrimonio/<int:pk>',list_patrimonio_especifc, name='list_patrimonio_especifc'),

    
    


]
