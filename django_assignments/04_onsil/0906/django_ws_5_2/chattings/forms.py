from turtle import textinput
from django import forms
from .models import Chat

class ChatForm(forms.ModelForm):

    user = forms.CharField(
        label = '사용자',
        widget = forms.TextInput(
            attrs = {
                'placeholder':'Nickname',
                'maxlength':10,
            }
        ),
    )

    content = forms.CharField(
        label = '내용',
        widget = forms.TextInput(
            attrs = {
                'rows':5,
                'cols':50,
                'placeholder':'Chat!',
            }
        ),
    )
    
    class Meta:
        model = Chat
        fields = '__all__'
