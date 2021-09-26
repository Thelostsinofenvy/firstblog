from blog import models
from django import forms
from django.forms import fields, widgets
from blog.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:  # more readable version!
        model = Post
        fields = ('author', 'title', 'Text')

   # meta = Post
    #fields = ('author', 'title', 'text')

    widgets = {'title': forms.TextInput(attrs={'class': 'textinputclass'}),
               'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea  postcontent'})
               }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'Text')
        widgets = {'author': forms.TextInput(attrs={'class': 'textinputclass'}),
                   'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea '})
                   }
