from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    """
    Model form, based on Post model, with title and text fields being the only editable ones.
    
    """
    class Meta:
        model = Post 
        fields = ("title",'text')
