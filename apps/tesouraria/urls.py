from django.urls import path
from .views import (conta_create, entrada_create)
urlpatterns = [
    #marcon
    path('despesa/create',conta_create, name='conta_create' ),
    path('entrada/create',entrada_create, name='entrada_create' ),




]
