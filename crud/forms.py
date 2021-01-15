from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
import re

from .models import Persona
class picture_form(forms.ModelForm):
    class Meta:
        model=Persona
        fields=('foto',)

class PersonaData(forms.Form):
    class meta:
        model = Persona
        fields = '__all__'
 
class RegistrationForm(forms.Form):
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}), label=_("Nombre"))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name'}), label=_("Apellido"))
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Usuario"), error_messages={'invalid': _("Este valor debe contener solo letras, números o guiones bajo.")})
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Contraseña"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Contraseña (de nuevo)"))
 
    def clean_username(self):
        try:
            User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("El nombre de usuario ya exisre. Por favor ingrese uno diferente."))

    def clean_email(self):
        try:
            User.objects.get(email__iexact=self.cleaned_data['email'])
        except User.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError(_("Email ya existe. Por favor ingrese uno diferente."))
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("Las contraseñas no coinciden."))
        return self.cleaned_data
