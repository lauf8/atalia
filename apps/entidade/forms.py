from .models import Membro, Patrimonio, CHOICES_PARENTESCO
from django import forms
from phonenumber_field.formfields import PhoneNumberField, RegionalPhoneNumberWidget




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
    demolay = forms.BooleanField(required=True)
    parentesco = forms.ChoiceField(choices=CHOICES_PARENTESCO ) 