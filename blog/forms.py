from django import forms

from .models import Post
from .models import Post2, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class PostForm2(forms.ModelForm):

    class Meta:
        model = Post2
        fields = ('title', 'f_choice', 'text',)
        
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
#        fields = ('author', 'text',)
        fields = ('text',)
