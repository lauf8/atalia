from django.shortcuts import render
from ..models import Entidade, Membro, Patrimonio
from apps.tesouraria.models import Arrecadacao, Contas
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404


@login_required
def list_everthing(request):
    despesas = Contas.objects.filter(user=request.user).all()
    entradas = Arrecadacao.objects.filter(user=request.user).all()
    membros = Membro.objects.filter(user=request.user).all().order_by('-id')[:5][::-1]
    patrimonios = Patrimonio.objects.filter(user=request.user).all().order_by('-id')[:5][::-1]
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

@login_required
def list_entidade_especific(request,pk):
    entidade = get_object_or_404(Entidade, pk=pk)
    
    despesas = Contas.objects.filter(entidade=entidade,user = request.user).all()
    entradas = Arrecadacao.objects.filter(entidade=entidade,user = request.user).all()
    if entidade.pk == 1:
        membros = Membro.objects.filter(user = request.user).all().order_by('-id')[:5][::-1]
    membros = []
    patrimonios = Patrimonio.objects.filter(entidade=entidade,user = request.user).all().order_by('-id')[:5][::-1]
    valor_despesas = []
    valor_entradas = []
    a = despesas
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



@login_required
def list_patrimonio(request):
    
    patrimonios = Patrimonio.objects.filter(user=request.user).all()
    context = {
        'patrimonios' : patrimonios,
        'title' : 'Patrimônios',
        
    }
        
    return render(request,'entidade/patrimonio/list_patrimonio.html', context)

@login_required
def list_patrimonio_especifc(request,pk):
    patrimonios = Patrimonio.objects.filter(entidade_id=pk,user = request.user).all()
    entidade = get_object_or_404(Entidade, pk=pk)
    title = "Patrimonios " +  entidade.nome 
    context = {
        'patrimonios' : patrimonios,
        'title' : title
        
    }
        
    return render(request,'entidade/patrimonio/list_patrimonio.html', context)

@login_required
def list_members(request):
    
    membros = Membro.objects.all()
    context = {
        'membros' : membros,
    }
        
    return render(request,'atalia/members.html', context)

@login_required
def list_members_especific(request,pk):
    entidade = get_object_or_404(Entidade, pk=pk)
    membros = Membro.objects.filter(entidade_id=entidade.pk,user=request.user).all()
    context = {
        'membros' : membros,
    }
        
    return render(request,'atalia/members.html', context)

@login_required
def show_members(request,pk):
    membro = get_object_or_404(Membro,pk=pk)
    if membro.user == request.user:
        context = {
            'membro' : membro,
        }
        return render(request,'entidade/membros/generics/show.html', context)
    raise Http404("A página que você está procurando não foi encontrada.")
@login_required
def show_patrimonio(request,pk):
    patrimonio = get_object_or_404(Patrimonio,pk=pk)
    if patrimonio.user == request.user:
        context = {
            'patrimonio' : patrimonio,
        }
        return render(request,'entidade/membros/generics/patrimonio.html', context)
    raise Http404("A página que você está procurando não foi encontrada.")