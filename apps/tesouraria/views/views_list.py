from django.shortcuts import render
from apps.entidade.forms import MarconForm, ClubeForm, DemolayForm, EscudeiroForm, FdjForm, AbelinhaForm, PatrimonioForm
from apps.entidade.models import Entidade, Membro, Patrimonio
from apps.tesouraria.models import Arrecadacao, Contas
from django.shortcuts import get_object_or_404



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



