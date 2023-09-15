from django.shortcuts import render
from ..forms import MarconForm, ClubeForm, DemolayForm, EscudeiroForm, FdjForm, AbelinhaForm, PatrimonioForm
from ..models import Entidade, Membro, Patrimonio
from apps.tesouraria.models import Arrecadacao, Contas
from django.shortcuts import get_object_or_404



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


def list_entidade_especific(request,pk):
    entidade = get_object_or_404(Entidade, pk=pk)
    despesas = Contas.objects.filter(entidade_id=entidade.pk).all()
    entradas = Arrecadacao.objects.filter(entidade_id=entidade.pk).all()
    membros = Membro.objects.filter(entidade_id=entidade.pk).all().order_by('-id')[:5][::-1]
    patrimonios = Patrimonio.objects.filter(entidade_id=entidade.pk).all().order_by('-id')[:5][::-1]
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
        'title' : entidade.nome,
        'entidade' : entidade,
        
    }
        
    return render(request,'entidade/membros/generics/index.html', context)




def list_patrimonio(request):
    
    patrimonios = Patrimonio.objects.all()
    context = {
        'patrimonios' : patrimonios,
        'title' : 'Patrimônios',
        
    }
        
    return render(request,'entidade/patrimonio/list_patrimonio.html', context)

def list_patrimonio_especifc(request,pk):
    patrimonios = Patrimonio.objects.filter(entidade_id=pk)
    entidade = get_object_or_404(Entidade, pk=pk)
    title = "Patrimonios " +  entidade.nome 
    context = {
        'patrimonios' : patrimonios,
        'title' : title
        
    }
        
    return render(request,'entidade/patrimonio/list_patrimonio.html', context)

def list_members(request):
    
    membros = Membro.objects.all()
    context = {
        'membros' : membros,
    }
        
    return render(request,'atalia/members.html', context)