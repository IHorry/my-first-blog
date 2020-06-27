from django import forms

from .models import *

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','coverImage', 'text')
        widgets = {
        	'title' : forms.TextInput(attrs={'placeholder': 'Enter Post title'}),
        	'text' : forms.Textarea(attrs={'placeholder' : 'Type your blog here...', 'oninput' : 'this.style.height = "";this.style.height = this.scrollHeight + "px"'})
        	
        }