from django import forms

class PostForm(forms.Form):
    image = forms.FileField()
    text = forms.CharField(widget=forms.Textarea(attrs={'cols': 48, 'rows': 3}), label="Description")