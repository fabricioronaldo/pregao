from django import forms
from notice.models import Edict, Platform, Status

class PlatformModelForm(forms.ModelForm):
  class Meta:
    model = Platform
    fields = ['name']
    labels = {
      'name':  'Plataforma'
    }
    widgets = {
      'name': forms.TextInput(attrs={
        'class': 'form-control form-control-solid',
        'placeholder': 'Nome da Plataforma'
      }),
    }

class StatusModelForm(forms.ModelForm):
  class Meta:
    model = Status
    fields = ['name']
    widgets = {
      'name': forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Nome do Status'
      })
    }
    