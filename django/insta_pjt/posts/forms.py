from django import forms
from .models import POST, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = POST
        exclude = (
            'user',
            'like_users',
        )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = (
            'user',
            'post',
        )