from django.shortcuts import render,redirect
from apps.entidade.forms import MarconForm, ClubeForm, DemolayForm, EscudeiroForm, FdjForm, AbelinhaForm, PatrimonioForm
from apps.entidade.models import Entidade, Membro, Patrimonio
from apps.tesouraria.models import Arrecadacao, Contas
from django.shortcuts import get_object_or_404
from ..forms import (ContaConfirmarPagamentoForms)
from django.contrib.auth.decorators import login_required



@login_required
def list_despesa(request):
    despesas = Contas.objects.all()
    valor_despesas = []
    
    for x in despesas:
        valor_despesas.append(x.valor)
    total_despesas = sum(valor_despesas)

    context = {
        'despesas' : despesas,
        'title' : 'Despesas',
        'total_despesas': total_despesas,
        
    }
        
    return render(request,'tesouraria/list/list_despesas.html', context)

@login_required
def list_despesa_especific(request, pk):
    entidade = get_object_or_404(Entidade, pk=pk)
    despesas = Contas.objects.filter(entidade_id = entidade.pk).all()
    valor_despesas = []
    
    for x in despesas:
        valor_despesas.append(x.valor)
    total_despesas = sum(valor_despesas)
    title = "Despesas " +  entidade.nome  

    context = {
        'despesas' : despesas,
        'title' : title,
        'total_despesas': total_despesas,
        
    }
        
    return render(request,'tesouraria/list/list_despesas.html', context)


@login_required
def list_entradas(request):
    entradas = Arrecadacao.objects.all()
    valor_entradas = []
    for x in entradas:
        valor_entradas.append(x.valor)
    total_entradas = sum(valor_entradas)
    context = {
        'entradas' : entradas,
        'total_entradas' : total_entradas,
        'title' : 'Arrecadações',
    }
        
    return render(request,'tesouraria/list/list_entradas.html', context)

@login_required
def list_entrada_especific(request,pk):
    entidade = get_object_or_404(Entidade, pk=pk)
    entradas = Arrecadacao.objects.filter(entidade_id = entidade.pk)
    valor_entradas = []
    for x in entradas:
        valor_entradas.append(x.valor)
    total_entradas = sum(valor_entradas)
    context = {
        'entradas' : entradas,
        'total_entradas' : total_entradas,
        'title' : 'Arrecadações ' + entidade.nome,
    }
        
    return render(request,'tesouraria/list/list_entradas.html', context)


@login_required
def show_conta(request,pk):
    
    conta = get_object_or_404(Contas,pk =pk)
    if request.method == "POST":
        form = ContaConfirmarPagamentoForms(request.POST, request.FILES)
        if form.is_valid():
            comprovante = form.cleaned_data['comprovante']
            conta.comprovante = comprovante
            conta.save()
            return redirect('show_conta', conta.pk) 
   
    else:
        form = ContaConfirmarPagamentoForms()
    context = {
            "form": form,
            'conta' : conta,
        }
    return render(request,'tesouraria/show/contas.html', context)


@login_required
def show_entrada(request,pk):
    entrada = get_object_or_404(Arrecadacao,pk =pk)
    context = {
        'arrecadacao' : entrada,
    }
    return render(request,'tesouraria/show/entradas.html', context)


