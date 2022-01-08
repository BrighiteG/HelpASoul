from django import forms
from django.forms import TextInput, CheckboxSelectMultiple

from blog.models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'profile_image', 'blog_tags']
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Adaugă un titlu', 'class': 'form-control'}),
            'description': TextInput(attrs={'placeholder': 'Adaugă descrierea', 'class': 'form-control'}),
            'blog_tags': CheckboxSelectMultiple()
        }
