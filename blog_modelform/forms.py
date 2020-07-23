from django import forms
from .models import Blogg

class BlogPost(forms.ModelForm):
    class Meta:
        model = Blogg
        fields = ['title','content']