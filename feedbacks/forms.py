"""from django import forms
from django.core.exceptions import ValidationError

from feedbacks.models import Feedback


class FeedbackModelForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('user', 'rating', 'text', 'created_at')

    def clean_name(self):
        try:
            Feedback.objects.get(name=self.cleaned_data['user'])


            Feedback.objects.get(name=self.cleaned_data['text'])
            raise ValidationError
        except Feedback.DoesNotExist:
            ...
        return self.cleaned_data['name']
"""
