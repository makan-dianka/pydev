
from django.forms import ModelForm
from django import forms
from .models import Pdf
class PdfForm(forms.ModelForm):
    class Meta:
        model = Pdf
        fields = ['langue', 'pdf', 'owner'] 

        widgets = {
            'langue': forms.Select(attrs={'class': 'form-control form-select', 'id':'lang-space'}),
            'owner': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'owner', 'type': 'hidden'}),
        }

        labels={'langue' : "Langue du Pdf", "pdf":"Document Pdf"}
        
        pdf = forms.FileField(),