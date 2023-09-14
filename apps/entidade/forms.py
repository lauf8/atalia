from .models import CHOICES_PARENTESCO, Entidade
from django import forms


CHOICES_SIM_OU_NAO = [
    (1, 'Sim'),
    (0, 'Não'),
   
]

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
    }))
    parentesco = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'form-control',
    }), choices=CHOICES_PARENTESCO)
    demolay = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'form-control',
    }), choices=CHOICES_SIM_OU_NAO)


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
        
    }))
    parentesco = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'form-control',
    }), choices=CHOICES_PARENTESCO)
    filha_de_jo = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'form-control',
    }), choices=CHOICES_SIM_OU_NAO)
    

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
    }))
    parentesco = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'form-control',
    }), choices=CHOICES_PARENTESCO)
    escudeiro = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'form-control',
    }), choices=CHOICES_SIM_OU_NAO)
    
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
    }))
    parentesco = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'form-control',
    }), choices=CHOICES_PARENTESCO)
    abelhinha = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'form-control',
    }), choices=CHOICES_SIM_OU_NAO)
    
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
    

