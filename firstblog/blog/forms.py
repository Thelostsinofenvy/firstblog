from typing import Text
from django import forms
from django.forms import widgets
from blog.models import Post, Comment


class PostForm(forms.ModelForm):
    meta = Post
    fields = ('author', 'title', 'text')

    widgets = {'title': forms.TextInput(attrs={'class': 'textinputclass'}),
               'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea  postcontent'})
               }


class CommentForm(forms.ModelForm):
    meta = Comment
    fields = ('author', 'text')
    widgets = {'author': forms.TextInput(attrs={'class': 'textinputclass'}),
               'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea '})
               }
