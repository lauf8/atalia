from django.shortcuts import render
from ..forms import MarconForm, ClubeForm, DemolayForm, EscudeiroForm, FdjForm, AbelinhaForm, PatrimonioForm
from ..models import Entidade, Membro, Patrimonio
from apps.tesouraria.models import Arrecadacao, Contas


def list_everthing(request):
    despesas = Contas.objects.all()
    entradas = Arrecadacao.objects.all()
    membros = Membro.objects.all().order_by('-id')[:5][::-1]
    patrimonios = Patrimonio.objects.all().order_by('-id')[:5][::-1]
    valor_despesas = []
    valor_entradas = []
    
    for x in despesas:
        valor_despesas.append(x.valor)
    
    for x in entradas:
        valor_entradas.append(x.valor)
        
    #lista as ultimas 5 tanto despesas quanto arrecadção
    despesas = despesas.order_by('-id')[:5][::-1] 
    entradas = entradas.order_by('-id')[:5][::-1]
    total_despesas = sum(valor_despesas)
    total_entradas = sum(valor_entradas)
    context = {
        'despesas' : despesas,
        'entradas' : entradas,
        'membros' : membros,
        'patrimonios' : patrimonios,
        'total_despesas' : total_despesas,
        'total_entradas' : total_entradas,
        'title' : 'Visão Geral',
        
    }
        
    return render(request,'atalia/index.html', context)


def list_marcon(request):
    despesas = Contas.objects.filter(entidade='Loja')
    entradas = Arrecadacao.objects.all(entidade='Loja')
    membros = Membro.objects.all().order_by('-id')[:5][::-1]
    patrimonios = Patrimonio.objects.all().order_by('-id')[:5][::-1]
    valor_despesas = []
    valor_entradas = []
    
    for x in despesas:
        valor_despesas.append(x.valor)
    
    for x in entradas:
        valor_entradas.append(x.valor)
        
    #lista as ultimas 5 tanto despesas quanto arrecadção
    despesas = despesas.order_by('-id')[:5][::-1] 
    entradas = entradas.order_by('-id')[:5][::-1]
    total_despesas = sum(valor_despesas)
    total_entradas = sum(valor_entradas)
    context = {
        'despesas' : despesas,
        'entradas' : entradas,
        'membros' : membros,
        'patrimonios' : patrimonios,
        'total_despesas' : total_despesas,
        'total_entradas' : total_entradas,
        'title' : 'Maçonaria',
        
    }
        
    return render(request,'entidade/membros/marcon/index.html', context)
