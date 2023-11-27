from django import forms
from apps.entidade.models import Entidade
from .models import Tipo_arrecadacao, Tipo_conta, Fornecedor, CHOICES_PIX
from ..entidade.forms import CHOICES_SIM_OU_NAO

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
    valor = forms.DecimalField()
    descricao = forms.CharField()
    pago = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'form-control',
    }), choices=CHOICES_SIM_OU_NAO)
    comprovante = forms.ImageField()
    
class FornecedorForm(forms.Form):
    nome = forms.CharField()
    celular = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    
    tipo_pix = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'form-control',
    }), choices=CHOICES_PIX)
    pix = forms.CharField(required=False)

    

class EntradaForms(forms.Form):
    
    entidade = forms.ModelChoiceField(widget=forms.Select(attrs={
        'class': 'form-control',
    }),queryset=Entidade.objects.all())
    tipo_arrecadacao = forms.ModelChoiceField(widget=forms.Select(attrs={
        'class': 'form-control',
    }),queryset=Tipo_arrecadacao.objects.all())
    pagador = forms.CharField()
    data_recebimento = forms.DateField(widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                }
            )
    )
    valor = forms.DecimalField()

    descricao = forms.CharField()

    pago = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'form-control',
    }), choices=CHOICES_SIM_OU_NAO)


class TipoEntradaForm(forms.Form):
    nome = forms.CharField()
    

class TipoSaidasForm(forms.Form):
    nome = forms.CharField()