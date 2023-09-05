from .models import CHOICES_PARENTESCO, Entidade
from django import forms


class MarconForm(forms.Form):
    nome = forms.CharField()
    data_nascimento = forms.DateField(widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                }
            )
    )
    endereco = forms.CharField()
    celular = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'data-mask': '000-000-000'
    }))
    parentesco = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'form-control',
    }), choices=CHOICES_PARENTESCO)
    demolay = forms.BooleanField(required=True)


class ClubeForm(forms.Form):
    nome = forms.CharField()
    data_nascimento = forms.DateField(widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                }
            )
    )
    endereco = forms.CharField()
    celular = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'data-mask': '000-000-000'
    }))
    parentesco = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'form-control',
    }), choices=CHOICES_PARENTESCO)
    filha_de_jo = forms.BooleanField(required=True)
    

class DemolayForm(forms.Form):
    nome = forms.CharField()
    data_nascimento = forms.DateField(widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                }
            )
    )
    endereco = forms.CharField()
    celular = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'data-mask': '000-000-000'
    }))
    parentesco = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'form-control',
    }), choices=CHOICES_PARENTESCO)
    escudeiro = forms.BooleanField(required=True)
    
class EscudeiroForm(forms.Form):
    nome = forms.CharField()
    data_nascimento = forms.DateField(widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                }
            )
    )
    endereco = forms.CharField()
    celular = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'data-mask': '000-000-000'
    }))
    parentesco = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'form-control',
    }), choices=CHOICES_PARENTESCO)
    
class FdjForm(forms.Form):
    nome = forms.CharField()
    data_nascimento = forms.DateField(widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                }
            )
    )
    endereco = forms.CharField()
    celular = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'data-mask': '000-000-000'
    }))
    parentesco = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'form-control',
    }), choices=CHOICES_PARENTESCO)
    abelhinha = forms.BooleanField(required=True)
    
class AbelinhaForm(forms.Form):
    nome = forms.CharField()
    data_nascimento = forms.DateField(widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                }
            )
    )
    endereco = forms.CharField()
    celular = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'data-mask': '000-000-000'
    }))
    parentesco = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'form-control',
    }), choices=CHOICES_PARENTESCO)
    
class PatrimonioForm(forms.Form):
    nome = forms.CharField()
    quantidade = forms.IntegerField()
    entidade = forms.ModelChoiceField(widget=forms.Select(attrs={
        'class': 'form-control',
    }),queryset=Entidade.objects.all())
    

