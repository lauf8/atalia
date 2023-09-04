from django.shortcuts import render
from atalia.settings import BASE_DIR
def home(response):
    print(BASE_DIR)
    return render(response, 'atalia/index.html')