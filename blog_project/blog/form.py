from django import forms
from .models import Post, Comment, Genre

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'genre']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']