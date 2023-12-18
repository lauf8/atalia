from django.urls import path
from .views.views_create import (patrimonio_create, create_member)
from .views.views_list import (list_everthing, list_patrimonio, list_patrimonio_especifc, 
                               list_entidade_especific, list_members, list_members_especific,
                               show_members,show_patrimonio)

urlpatterns = [
    
    path('',list_everthing, name='list_everthing' ),
    path('<int:pk>',list_entidade_especific, name='list_entidade_especific'),
    path('membros',list_members, name='list_members'),
    path('membros/<int:pk>',list_members_especific, name='list_members_especific'),
    path('membros/create',create_member, name='create_member'),
    path('membros/<int:pk>/show',show_members, name='show_membro'),
    
    #patrimonio
    path('patrimonio/create',patrimonio_create, name='patrimonio_create'),
    path('patrimonio',list_patrimonio, name='list_patrimonio'),
    path('patrimonio/<int:pk>',list_patrimonio_especifc, name='list_patrimonio_especific'),
    path('patrimonio/<int:pk>/show',show_patrimonio, name='show_patrimonio'),

]
