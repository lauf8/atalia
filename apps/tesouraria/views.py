from django.shortcuts import render
from .forms import ContaForms

def conta_create(request):
    if request.method == "POST":
        form = ContaForms(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            
            
    else:
        form = ContaForms()
    context = {
            "form": form,
            "title": 'Cadastrar Conta',
            "title_form" : 'Cadastrar Conta'
        }
    
    return render(request, 'tesouraria/form.html', context)
