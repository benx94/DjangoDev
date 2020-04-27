from django.forms import ModelForm, TextInput, EmailInput
from django.forms.utils import ErrorList

from .models import Materiel, Owner, Test


class ParagraphErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()
    def as_divs(self):
        if not self: return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<p class="small error">%s</p>' % e for e in self])

class InventoryAddForm(ModelForm):
    class Meta:
        model = Test
        fields = ["login", "telephone", "prenom", "nom"]
        widgets = {
            'login': TextInput(attrs={'class': 'form-control'}),
            'nom': TextInput(attrs={'class': 'form-control'}),
            'prenom': TextInput(attrs={'class': 'form-control'}),
            'telephone': TextInput(attrs={'class': 'form-control'})
        }

class InventoryAddNewForm(ModelForm):
    class Meta:
        model = Test
        fields = ["machine", "login", "ip", "telephone", "prenom", "nom"]
        widgets = {
            'machine': TextInput(attrs={'class': 'form-control'}),
            'login': TextInput(attrs={'class': 'form-control'}),
            'ip': TextInput(attrs={'class': 'form-control'}),
            'nom': TextInput(attrs={'class': 'form-control'}),
            'prenom': TextInput(attrs={'class': 'form-control'}),
            'telephone': TextInput(attrs={'class': 'form-control'})
        }
