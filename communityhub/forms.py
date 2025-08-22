from django import forms
from .models import Post, Comment, Group
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description']



