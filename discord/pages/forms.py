from django import forms
from .models import Project

# Categories settings


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'body', 'header_image',
                  'website_link', 'repository_link')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'website_link': forms.TextInput(attrs={'class': 'form-control'}),
            'repository_link': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'body', 'header_image',
                  'website_link', 'repository_link')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'website_link': forms.TextInput(attrs={'class': 'form-control'}),
            'repository_link': forms.TextInput(attrs={'class': 'form-control'}),
        }
