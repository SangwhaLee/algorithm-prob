from django import forms
from .models import Movie, Comment, Hashtag


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        # fields = '__all__'
        fields = ('title', 'content',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ('movie', 'user',)


class HashtagForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'