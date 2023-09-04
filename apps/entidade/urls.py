from django.urls import path
from .views import create_marcon
urlpatterns = [
    path('marcon/create',create_marcon, name='create_marcon' )
]
