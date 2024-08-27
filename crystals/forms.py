from django import forms
from .models import Crystal

class CrystalForm(forms.ModelForm):
    class Meta:
        model = Crystal
        fields = ['name', 'age', 'location', 'is_active']