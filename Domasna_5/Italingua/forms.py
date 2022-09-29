from django import forms
from .models import UserPerson, ForumQuestion, Comment


class QuestionForm(forms.ModelForm):
    class Meta:
        model = ForumQuestion
        exclude = {'numberOfReplies'}


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
