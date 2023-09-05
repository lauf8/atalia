from django.urls import path
from .views import (conta_create, entrada_create,fornecedor_create )
urlpatterns = [
    #marcon
    path('despesa/create',conta_create, name='conta_create' ),
    path('entrada/create',entrada_create, name='entrada_create' ),
    path('fornecedor/create',fornecedor_create, name='fornecedor_create' ),


]
