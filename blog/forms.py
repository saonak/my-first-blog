from django import forms

from .models import Post
from .models import Post2, Comment
from .models import Title, PostJ, CommentJ, Presentation, Test, CommentP


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

class TitleForm(forms.ModelForm):

    class Meta:
        model = Title
#        fields = ('author', 'text',)
        fields = ('title','subtitle1','subtitle2','subtitle3','subtitle4')

class PostJForm(forms.ModelForm):

    class Meta:
        model = PostJ
        fields = ('f_choice', 'text',)

class CommentJForm(forms.ModelForm):

    class Meta:
        model = CommentJ
#        fields = ('author', 'text',)
        fields = ('text',)

class PresentationForm(forms.ModelForm):

    class Meta:
        model = Presentation
        fields = ('f_choice', 'text',)

class TestForm(forms.ModelForm):

    class Meta:
        model = Test
        fields = ('f_choice', 'text',)

class CommentPForm(forms.ModelForm):

    class Meta:
        model = CommentP
#        fields = ('author', 'text',)
        fields = ('text',)
