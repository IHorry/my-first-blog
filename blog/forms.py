from django import forms

from .models import *

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','coverImage', 'text')
        widgets = {
        	'title' : forms.TextInput(attrs={'placeholder': 'Enter Post title'}),
        	'text' : forms.Textarea(attrs={'placeholder' : 'Type your blog here...', 'oninput' : 'this.style.height = "";this.style.height = this.scrollHeight + "px"','class':  'textarea'})
        	
        }



class CVForm(forms.ModelForm):

    class Meta:
        model = CV
        fields = ('summary','interests','references')
        widgets = {
        	'summary' : forms.Textarea(attrs={'placeholder': 'Enter Summary here','oninput' : 'this.style.height = "";this.style.height = this.scrollHeight + "px"','class':  'textarea'}),
        	'interests' : forms.Textarea(attrs={'placeholder': 'Type here','oninput' : 'this.style.height = "";this.style.height = this.scrollHeight + "px"','class':  'textarea'}),
        	'references' : forms.Textarea(attrs={'placeholder': 'Type here','oninput' : 'this.style.height = "";this.style.height = this.scrollHeight + "px"','class':  'textarea'})
        }






class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = {'skill','description'}
        widgets = {
            'skill' : forms.TextInput(attrs={'placeholder': 'Skill Name','oninput' : 'this.style.height = "";this.style.height = this.scrollHeight + "px"',}),
            'description' : forms.TextInput(attrs={'placeholder': 'Skill description' , 'oninput' :'this.style.height = "";this.style.height = this.scrollHeight + "px"','class':  'textarea'})
  
        }



class QualForm(forms.ModelForm):
    class Meta:
        model = Qual
        fields = {'qualification','subject','grade'}
        widgets = {
            'qualification' : forms.TextInput(attrs={'placeholder': 'Qualification','oninput' : 'this.style.height = "";this.style.height = this.scrollHeight + "px"',}),
            'subject' : forms.TextInput(attrs={'placeholder': 'Area of Study' , 'oninput' :'this.style.height = "";this.style.height = this.scrollHeight + "px"'}),
            'grade' : forms.TextInput(attrs={'placeholder': 'Grade Achieved' , 'oninput' :'this.style.height = "";this.style.height = this.scrollHeight + "px"'})

  
        }




class WorkForm(forms.ModelForm):
    dateStarted = forms.DateField(input_formats=['%d/%m/%Y'])
    dateEnd = forms.DateField(input_formats=['%d/%m/%Y'])
    class Meta:
        model = Work
        fields = {'title','company','dateStarted','dateEnd'}
        widgets = {
            'title' : forms.TextInput(attrs={'placeholder': 'Job title','oninput' : 'this.style.height = "";this.style.height = this.scrollHeight + "px"','class':  'textarea'}),
            'company' : forms.TextInput(attrs={'placeholder': 'Company Name' , 'oninput' :'this.style.height = "";this.style.height = this.scrollHeight + "px"','class':  'textarea'}),
            'dateStarted' : forms.DateInput(attrs={'class': 'form-control datetimepicker-input', 'data-target': '#datetimepicker1'}),
            'dateEnd' : forms.DateInput(attrs={'class': 'form-control datetimepicker-input', 'data-target': '#datetimepicker2'})
  
        }