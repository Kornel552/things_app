from django import forms
from .models import Comment
from .models import Lista

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'post']


class ListaForm(forms.ModelForm):
    class Meta:
        model = Lista
        fields = ['title']

class MyForm(forms.Form):
    my_field = forms.CharField(widget=forms.TextInput(attrs={'class': 'my-custom-class'}))