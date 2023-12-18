from .models import CHOICES_PARENTESCO, Entidade
from django import forms


CHOICES_SIM_OU_NAO = [
    (1, 'Sim'),
    (0, 'Não'),
   
]

class MemberForm(forms.Form):
    entidade = forms.ModelChoiceField(widget=forms.Select(attrs={
        'class': 'form-control',
    }),queryset=Entidade.objects.all())
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
    

