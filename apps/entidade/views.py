from django.shortcuts import render
from .forms import MarconForm
from .models import Entidade, Membro


def create_marcon(request):
    if request.method == "POST":
        form = MarconForm(request.POST)
        if form.is_valid():
            entidade = Entidade.objects.get(pk=1)
            nome = form.cleaned_data['nome']
            data_nascimento = form.cleaned_data['data_nascimento']
            endereco = form.cleaned_data['endereco']
            celular = form.cleaned_data['celular']
            parentesco = form.cleaned_data['parentesco']
            demolay = form.cleaned_data['demolay']
            marcon = True
            membro = Membro() 
            membro.entidade = entidade
            membro.nome = nome
            membro.data_nascimento = data_nascimento
            membro.endereco = endereco
            membro.celular = celular
            membro.parentesco_maconico = parentesco
            membro.demolay = demolay
            membro.marcon = marcon
            membro.save()

    else:
        form = MarconForm()

    context = {
        "form": form
    }

    return render(request, 'entidade/form.html', context)


