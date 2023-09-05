from django.urls import path
from .views import (create_marcon)
urlpatterns = [
    #marcon
    path('despesa/create',create_marcon, name='create_marcon' ),



]
