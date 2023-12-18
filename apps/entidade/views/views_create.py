from django.shortcuts import redirect, render
from ..forms import (PatrimonioForm, MemberForm,MensalidadeForm)
from ..models import Entidade, Membro, Patrimonio
from apps.tesouraria.models import Arrecadacao, Contas
from django.contrib.auth.decorators import login_required



@login_required(redirect_field_name='login')
def patrimonio_create(request):
    if request.method == "POST":
        form = PatrimonioForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            quantidade = form.cleaned_data['quantidade']
            entidade = form.cleaned_data['entidade']
            patrimonio = Patrimonio()
            patrimonio.nome = nome
            patrimonio.quantidade = quantidade
            patrimonio.entidade = entidade
            patrimonio.user = request.user
            patrimonio.save()
            return redirect('list_patrimonio') 
            
    else:
        form = PatrimonioForm()
    context = {
            "form": form
        }
    
    return render(request, 'entidade/patrimonio/form.html', context)

@login_required(redirect_field_name='login')
def create_member(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            cpf = form.cleaned_data['cpf']
            data_nascimento = form.cleaned_data['data_nascimento']
            endereco = form.cleaned_data['endereco']
            celular = form.cleaned_data['celular']
            membro = Membro() 
            membro.nome = nome
            membro.data_nascimento = data_nascimento
            membro.endereco = endereco
            membro.celular = celular
            membro.cpf = cpf
            membro.user = request.user
            membro.save()
            return redirect('list_members') 

    else:
        form = MemberForm()

    context = {
        "form": form
    }

    return render(request, 'entidade/membros/generics/form.html', context)


def create_mensalidade(request):
    if request.method == "POST":
        form = MensalidadeForm(request.POST)
        if form.is_valid():
            return redirect('list_members') 

    else:
        form = MensalidadeForm()

    context = {
        "form": form
    }

    return render(request, 'entidade/membros/generics/form.html', context)



