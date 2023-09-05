from django import forms
from apps.entidade.models import Entidade
from .models import Tipo_arrecadacao, Tipo_conta, Fornecedor

class ContaForms(forms.Form):
    
    entidade = forms.ModelChoiceField(widget=forms.Select(attrs={
        'class': 'form-control',
    }),queryset=Entidade.objects.all())
    tipo_despesa = forms.ModelChoiceField(widget=forms.Select(attrs={
        'class': 'form-control',
    }),queryset=Tipo_conta.objects.all())
    fornecedor = forms.ModelChoiceField(widget=forms.Select(attrs={
        'class': 'form-control',
    }),queryset=Fornecedor.objects.all())
    data_recebimento_da_conta = forms.DateField(widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                }
            )
    )
    valor = forms.IntegerField()
    pagamento = forms.BooleanField()
    descricao = forms.Textarea()
    