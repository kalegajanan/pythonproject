from django import forms
from modelformapp.models import project

class ProjectForm(forms.ModelForm):
    class Meta:
        model=project
        fields='__all__'
    
