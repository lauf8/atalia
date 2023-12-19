from django.shortcuts import redirect, render
from ..forms import (PatrimonioForm, MemberForm,MensalidadeForm, PercaptaForm)
from ..models import Entidade, Membro, Patrimonio, Percapta, Mensalidade
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


def create_percapta(request):
    if request.method == "POST":
        form = PercaptaForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            captacao = form.cleaned_data['captacao']
            cmsb = form.cleaned_data['cmsb']
            cmi = form.cleaned_data['cmi']
            fdj_gleb = form.cleaned_data['fdj_gleb']
            dm_gleb = form.cleaned_data['dm_gleb']
            reforma = form.cleaned_data['reforma']
            dm_atalaia = form.cleaned_data['dm_atalaia']
            fdj_atalia = form.cleaned_data['fdj_atalia']

            percapta = Percapta()
            percapta.nome = nome
            percapta.captacao = captacao
            percapta.cmsb = cmsb
            percapta.cmi = cmi
            percapta.fdj_gleb = fdj_gleb
            percapta.dm_gleb = dm_gleb
            percapta.reforma = reforma
            percapta.dm_atalaia = dm_atalaia
            percapta.fdj_atalia = fdj_atalia
            percapta.user = request.user
            percapta.save()

            return redirect('list_members') 

    else:
        form = PercaptaForm()

    context = {
        "form": form
    }

    return render(request, 'entidade/membros/generics/form.html', context)


def create_mensalidade(request):
    if request.method == "POST":
        form = MensalidadeForm(request.POST,request.FILES)
        if form.is_valid():

            membro = form.cleaned_data['membro']
            percapta = form.cleaned_data['percapta']
            comprovante = form.cleaned_data['comprovante']
            valor = form.cleaned_data['valor']
            data = form.cleaned_data['data']

            mensalidade = Mensalidade()
            mensalidade.membro = membro  
            mensalidade.percapta = percapta  
            mensalidade.comprovante = comprovante  
            mensalidade.valor = valor 
            mensalidade.data = data  
            mensalidade.save()
            #if mensalidade.save():
            
            
            return redirect('list_members') 

    else:
        form = MensalidadeForm()

    context = {
        "form": form
    }

    return render(request, 'entidade/membros/generics/form_mensalidade.html', context)

 