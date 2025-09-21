from django import forms
from main.models import *


class MuallifForm(forms.ModelForm):
    class Meta:
        model = Muallif
        fields = "__all__"
        widgets = {
            'tugilgan_sana': forms.DateInput(attrs={'type': 'date'})
        }
