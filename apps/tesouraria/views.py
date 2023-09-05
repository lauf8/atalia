from django.shortcuts import render
from .forms import ContaForms, EntradaForms
from .models import Contas, Arrecadacao

def conta_create(request):
    if request.method == "POST":
        form = ContaForms(request.POST)
        if form.is_valid():
            entidade = form.cleaned_data['entidade']
            tipo_despesa = form.cleaned_data['tipo_despesa']
            fornecedor = form.cleaned_data['fornecedor']
            data_recebimento_da_conta = form.cleaned_data['data_recebimento_da_conta']
            valor = form.cleaned_data['valor']
            descricao = form.cleaned_data['descricao']
            pago = form.cleaned_data['pago']
    
    
            conta = Contas()
            conta.entidade = entidade
            conta.tipo_despesa = tipo_despesa
            conta.fornecedor = fornecedor
            conta.data_recebimento = data_recebimento_da_conta
            conta.valor = valor
            conta.descricao = descricao
            conta.pagamento = pago
            conta.save()
            

            
    else:
        form = ContaForms()
    context = {
            "form": form,
            "title": 'Cadastrar Entrada',
            "title_form" : 'Cadastrar Entrada'
        }
    
    return render(request, 'tesouraria/form.html', context)


def entrada_create(request):
    if request.method == "POST":
        form = EntradaForms(request.POST)
        if form.is_valid():
            entidade = form.cleaned_data['entidade']
            tipo_arrecadacao = form.cleaned_data['tipo_arrecadacao']
            pagador = form.cleaned_data['pagador']
            data_recebimento = form.cleaned_data['data_recebimento']
            valor = form.cleaned_data['valor']
            descricao = form.cleaned_data['descricao']
            pago = form.cleaned_data['pago']
            entrada = Arrecadacao()
            entrada.entidade = entidade
            entrada.tipo_arrecadacao = tipo_arrecadacao
            entrada.pagador = pagador
            entrada.data_recebimento = data_recebimento
            entrada.valor = valor
            entrada.descricao = descricao
            entrada.pagamento = pago
            entrada.save()
            

            
    else:
        form = EntradaForms()
    context = {
            "form": form,
            "title": 'Cadastrar Entrada',
            "title_form" : 'Cadastrar Entrada'
        }
    
    return render(request, 'tesouraria/form.html', context)