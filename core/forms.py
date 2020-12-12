from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5})
        }