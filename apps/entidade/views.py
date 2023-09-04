from django.shortcuts import render
from .forms import MarconForm


def create_marcon(request):
    if request.method == "POST":
        form = MarconForm(request.POST)
        if form.is_valid():
            carro = form.cleaned_data['carro']

    else:
        form = MarconForm()

    context = {
        "form": form
    }

    return render(request, 'entidade/form.html', context)
