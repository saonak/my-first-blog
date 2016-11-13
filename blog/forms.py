from django import forms
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple

from .models import Post
from .models import Post2, Comment
from .models import Title, PostJ, CommentJ, Presentation, Test, CommentP
from .models import Expert


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

class ExpertForm(forms.ModelForm):

    class Meta:
        model = Expert
        fields = ('group','user1','user2','user3','user4')

class ExpertFormGroup(forms.Form):
    group = forms.ChoiceField(label='Groupの選択', widget=forms.Select, choices=(), required=False, )

class ExpertFormUser(forms.Form):
    user1 = forms.ChoiceField(label='Expertの選択', widget=forms.Select, choices=(), required=False, )
    user2 = forms.ChoiceField(label='Expertの選択', widget=forms.Select, choices=(), required=False, )
    user3 = forms.ChoiceField(label='Expertの選択', widget=forms.Select, choices=(), required=False, )
    user4 = forms.ChoiceField(label='Expertの選択', widget=forms.Select, choices=(), required=False, )

class TopicSelForm(forms.Form):
    titlenum = forms.ChoiceField( label = 'Topicの選択', initial= '1', widget = forms.Select, choices = (), required = False,)