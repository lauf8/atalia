from django.shortcuts import redirect, render
from ..forms import (MarconForm, ClubeForm, DemolayForm, EscudeiroForm, FdjForm, AbelinhaForm, 
                    PatrimonioForm, MemberForm)
from ..models import Entidade, Membro, Patrimonio
from apps.tesouraria.models import Arrecadacao, Contas
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='login')
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

    return render(request, 'entidade/membros/marcon/form.html', context)

@login_required(redirect_field_name='login')
def clube_fraternidade_create(request):
    if request.method == "POST":
        form = ClubeForm(request.POST)
        if form.is_valid():
            entidade = Entidade.objects.get(pk=2)
            nome = form.cleaned_data['nome']
            data_nascimento = form.cleaned_data['data_nascimento']
            endereco = form.cleaned_data['endereco']
            celular = form.cleaned_data['celular']
            parentesco = form.cleaned_data['parentesco']
            filha_de_jo = form.cleaned_data['filha_de_jo']
            clube_da_fraternidade = True
            membro = Membro() 
            membro.entidade = entidade
            membro.nome = nome
            membro.data_nascimento = data_nascimento
            membro.endereco = endereco
            membro.celular = celular
            membro.parentesco_maconico = parentesco
            membro.fdj = filha_de_jo
            membro.clube_da_fraternidade = clube_da_fraternidade
            membro.save()

    else:
        form = ClubeForm()

    context = {
        "form": form
    }

    return render(request, 'entidade/membros/clube_da_fraternidade/form.html', context)

@login_required(redirect_field_name='login')
def demolay_create(request):
    if request.method == "POST":
        form = DemolayForm(request.POST)
        if form.is_valid():
            entidade = Entidade.objects.get(pk=3)
            nome = form.cleaned_data['nome']
            data_nascimento = form.cleaned_data['data_nascimento']
            endereco = form.cleaned_data['endereco']
            celular = form.cleaned_data['celular']
            parentesco = form.cleaned_data['parentesco']
            escudeiro = form.cleaned_data['escudeiro']
            demolay = True
            membro = Membro() 
            membro.entidade = entidade
            membro.nome = nome
            membro.data_nascimento = data_nascimento
            membro.endereco = endereco
            membro.celular = celular
            membro.parentesco_maconico = parentesco
            membro.demolay = demolay
            membro.escudeiro = escudeiro
            membro.save()

    else:
        form = DemolayForm()

    context = {
        "form": form
    }

    return render(request, 'entidade/membros/demolay/form.html', context)
@login_required(redirect_field_name='login')
def escudeiro_create(request):
    if request.method == "POST":
        form = EscudeiroForm(request.POST)
        if form.is_valid():
            entidade = Entidade.objects.get(pk=4)
            nome = form.cleaned_data['nome']
            data_nascimento = form.cleaned_data['data_nascimento']
            endereco = form.cleaned_data['endereco']
            celular = form.cleaned_data['celular']
            parentesco = form.cleaned_data['parentesco']
            escudeiro = form.cleaned_data['escudeiro']
            escudeiro = True
            membro = Membro() 
            membro.entidade = entidade
            membro.nome = nome
            membro.data_nascimento = data_nascimento
            membro.endereco = endereco
            membro.celular = celular
            membro.parentesco_maconico = parentesco
            membro.escudeiro = escudeiro
            membro.save()

    else:
        form = EscudeiroForm()

    context = {
        "form": form
    }

    return render(request, 'entidade/membros/escudeiro/form.html', context)


@login_required(redirect_field_name='login')
def fdj_create(request):
    if request.method == "POST":
        form = FdjForm(request.POST)
        if form.is_valid():
            entidade = Entidade.objects.get(pk=5)
            nome = form.cleaned_data['nome']
            data_nascimento = form.cleaned_data['data_nascimento']
            endereco = form.cleaned_data['endereco']
            celular = form.cleaned_data['celular']
            parentesco = form.cleaned_data['parentesco']
            abelinha = form.cleaned_data['abelinha']
            fdj = True
            membro = Membro() 
            membro.entidade = entidade
            membro.nome = nome
            membro.data_nascimento = data_nascimento
            membro.endereco = endereco
            membro.celular = celular
            membro.parentesco_maconico = parentesco
            membro.fdj = fdj
            membro.abelhinha = abelinha
            membro.save()

    else:
        form = FdjForm()

    context = {
        "form": form
    }

    return render(request, 'entidade/membros/fdj/form.html', context)


@login_required(redirect_field_name='login')
def abelinha_create(request):
    if request.method == "POST":
        form = AbelinhaForm(request.POST)
        if form.is_valid():
            entidade = Entidade.objects.get(pk=6)
            nome = form.cleaned_data['nome']
            data_nascimento = form.cleaned_data['data_nascimento']
            endereco = form.cleaned_data['endereco']
            celular = form.cleaned_data['celular']
            parentesco = form.cleaned_data['parentesco']
            abelhinha = True
            membro = Membro() 
            membro.entidade = entidade
            membro.nome = nome
            membro.data_nascimento = data_nascimento
            membro.endereco = endereco
            membro.celular = celular
            membro.parentesco_maconico = parentesco
            membro.abelhinha = abelhinha
            membro.save()

    else:
        form = AbelinhaForm()

    context = {
        "form": form
    }

    return render(request, 'entidade/membros/comeia/form.html', context)

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
            entidade = form.cleaned_data['entidade']
            nome = form.cleaned_data['nome']
            data_nascimento = form.cleaned_data['data_nascimento']
            endereco = form.cleaned_data['endereco']
            celular = form.cleaned_data['celular']
            parentesco = form.cleaned_data['parentesco']
            membro = Membro() 
            membro.entidade = entidade
            membro.nome = nome
            membro.data_nascimento = data_nascimento
            membro.endereco = endereco
            membro.celular = celular
            membro.parentesco_maconico = parentesco
            membro.save()
            return redirect('list_members') 

    else:
        form = MemberForm()

    context = {
        "form": form
    }

    return render(request, 'entidade/membros/generics/form.html', context)