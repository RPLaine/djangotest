from django import forms
from .models import SimpleData

class SimpleDataForm(forms.ModelForm):
    class Meta:
        model = SimpleData
        fields = ['content']
        widgets = {'content': forms.TextInput(attrs= {'autofocus': True})}