from django import forms

class CreatePostForm(forms.Form):
    description = forms.CharField(label="description", max_length=200)
    image = forms.ImageField()
    
