from tkinter import Widget
from django import forms
from .models import Question, Comment

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        widgets = {
            'title':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'title'
                }
            ),
            'RED_TEAM':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'RED_TEAM'
                }
            ),
            'BLUE_TEAM':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'BLUE_TEAM'
                }
            ),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('question',)
        TEAM_PICK = (
            ('', 'SELECT'),
            ('RED TEAM','RED TEAM'),
            ('BLUE TEAM','BLUE TEAM'),
        ) 
        widgets = {
            'pick': forms.Select(
                choices=TEAM_PICK,
                attrs= {
                    'class':'form-control',
                }
            ),
            'content': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Content'
                }
            ),
        }