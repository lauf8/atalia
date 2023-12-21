import datetime
from django.shortcuts import redirect, render
from ..forms import (PatrimonioForm, MemberForm,MensalidadeForm, PercaptaForm)
from ..models import Entidade, Membro, Patrimonio, Percapta, Mensalidade
from apps.tesouraria.models import Arrecadacao, Contas, Tipo_arrecadacao, Tipo_conta
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from helps.idade import idade_do_usuario
import datetime
#from helps.idade import idade_do_usuario


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
            mensalidade.percapita = percapta  
            mensalidade.comprovante = comprovante  
            mensalidade.valor = valor 
            mensalidade.data_pagamento = data  
            mensalidade.user = request.user

            mensalidade.save()
            if mensalidade.pk is not None:
                qtd_membros = Membro.objects.count()
                taxa = round((mensalidade.percapita.cmi + mensalidade.percapita.cmsb) /qtd_membros, 2)

                idade = idade_do_usuario(mensalidade.membro.data_nascimento)
                if idade > 25:            
                    conta_gleb = Contas()
                    conta_gleb.valor = (taxa + mensalidade.percapita.dm_gleb + mensalidade.percapita.captacao +
                                        mensalidade.percapita.fdj_gleb)
                    conta_gleb.entidade = get_object_or_404(Entidade,pk=1)
                    conta_gleb.tipo_despesa = get_object_or_404(Tipo_conta,pk=1)
                    conta_gleb.data_recebimento = datetime.date.today()
                    conta_gleb.pagamento = True
                    conta_gleb.descricao = 'Mensalidade'
                    conta_gleb.user = mensalidade.user
                    conta_gleb.save()
                    taxa += (mensalidade.percapita.dm_gleb + mensalidade.percapita.captacao +
                                        mensalidade.percapita.fdj_gleb)
                else:
                    conta_gleb = Contas()
                    conta_gleb.valor = (taxa)
                    conta_gleb.entidade = get_object_or_404(Entidade,pk=1)
                    conta_gleb.tipo_despesa = get_object_or_404(Tipo_conta,pk=1)
                    conta_gleb.data_recebimento = datetime.date.today()
                    conta_gleb.pagamento = True
                    conta_gleb.descricao = 'Mensalidade'
                    conta_gleb.user = mensalidade.user
                    conta_gleb.save()
                    

                conta_dm = Contas()
                conta_dm.valor = mensalidade.percapita.dm_atalaia
                conta_dm.entidade = get_object_or_404(Entidade,pk=1)
                conta_dm.tipo_despesa = get_object_or_404(Tipo_conta,pk=2)
                conta_dm.data_recebimento = datetime.date.today()
                conta_dm.pagamento = True
                conta_dm.descricao = 'Mensalidade DeMolay'
                conta_dm.user = mensalidade.user
                conta_dm.save()

                arrecadao_dm = Arrecadacao()
                arrecadao_dm.data_recebimento = datetime.date.today()
                arrecadao_dm.valor = conta_dm.valor
                arrecadao_dm.pagador = mensalidade.membro.nome
                arrecadao_dm.entidade = get_object_or_404(Entidade,pk=3)
                arrecadao_dm.descricao = 'Mensalidade'
                arrecadao_dm.pagamento = True
                arrecadao_dm.user = request.user
                arrecadao_dm.save()



                conta_fdj = Contas()
                conta_fdj.valor = mensalidade.percapita.fdj_atalia
                conta_fdj.entidade = get_object_or_404(Entidade,pk=1)
                conta_fdj.tipo_despesa = get_object_or_404(Tipo_conta,pk=3)
                conta_fdj.data_recebimento = datetime.date.today()
                conta_fdj.pagamento = True
                conta_fdj.descricao = 'Mensalidade FDJ'
                conta_fdj.user = mensalidade.user
                conta_fdj.save()

                arrecadao_fdj = Arrecadacao()
                arrecadao_fdj.data_recebimento = datetime.date.today()
                arrecadao_fdj.valor = conta_fdj.valor
                arrecadao_fdj.pagador = mensalidade.membro.nome
                arrecadao_fdj.entidade = get_object_or_404(Entidade,pk=5)
                arrecadao_fdj.descricao = 'Mensalidade'
                arrecadao_fdj.pagamento = True
                arrecadao_fdj.user = request.user
                arrecadao_fdj.save()

                arrecadao_loja = Arrecadacao()
                arrecadao_loja.data_recebimento = datetime.date.today()
                arrecadao_loja.valor = mensalidade.valor - (taxa +  arrecadao_fdj.valor + arrecadao_dm.valor)
                arrecadao_loja.pagador = mensalidade.membro.nome
                arrecadao_loja.entidade = get_object_or_404(Entidade,pk=1)
                arrecadao_loja.descricao = 'Mensalidade'
                arrecadao_loja.pagamento = True
                arrecadao_loja.user = request.user
                arrecadao_loja.save()

            return redirect('list_members') 

    else:
        form = MensalidadeForm()

    context = {
        "form": form
    }

    return render(request, 'entidade/membros/generics/form_mensalidade.html', context)

 