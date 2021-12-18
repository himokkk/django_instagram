from django import forms

class CommentForm(forms.Form):
    comment = forms.CharField(max_length=200)

