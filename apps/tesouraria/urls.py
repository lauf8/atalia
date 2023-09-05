from django.urls import path
from .views import (conta_create)
urlpatterns = [
    #marcon
    path('despesa/create',conta_create, name='conta_create' ),



]
