from django import forms

from .models import Choice, Question

class CreateQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'category',]

class CreateChoicesForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']