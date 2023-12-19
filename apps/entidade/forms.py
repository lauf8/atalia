from .models import  Entidade, Membro, Percapta
from django import forms
from django_select2.forms import ModelSelect2Widget


CHOICES_SIM_OU_NAO = [
    (1, 'Sim'),
    (0, 'Não'),
   
]


class MemberForm(forms.Form):


    nome = forms.CharField()
    data_nascimento = forms.DateField(widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                }
            )
    )
    endereco = forms.CharField()    
    cpf = forms.CharField(max_length=14)   
    celular = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))



    
class PatrimonioForm(forms.Form):


    nome = forms.CharField()
    quantidade = forms.IntegerField()
    entidade = forms.ModelChoiceField(widget=forms.Select(attrs={
        'class': 'form-control',
    }),queryset=Entidade.objects.all())
    


class PercaptaForm(forms.Form):


    nome = forms.CharField()
    captacao = forms.DecimalField()
    cmsb = forms.DecimalField()
    cmi = forms.DecimalField()
    fdj_gleb = forms.DecimalField()
    dm_gleb = forms.DecimalField()
    reforma = forms.DecimalField()
    dm_atalaia = forms.DecimalField()
    fdj_atalia = forms.DecimalField()


class MensalidadeForm(forms.Form):


    membro = forms.ModelChoiceField(
        queryset=Membro.objects.all(),
        widget=ModelSelect2Widget(
            model=Membro,
            search_fields=['nome__icontains'],
            attrs={'class': 'form-control select2', 'style': 'width: 100%;'},
        )
    )
    percapta = forms.ModelChoiceField(widget=forms.Select(attrs={
        'class': 'form-control',
    }),queryset=Percapta.objects.all())
    comprovante = forms.ImageField(required=False)
    valor = forms.DecimalField()
    data = forms.DateField(widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                }
            )
    )
