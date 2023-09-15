from django.urls import path
from .views.views_create import (create_marcon, clube_fraternidade_create, demolay_create, escudeiro_create,
                    fdj_create, abelinha_create, patrimonio_create)
from .views.views_list import (list_everthing)

urlpatterns = [
    
    path('',list_everthing, name='list_everthing' ),

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


]
