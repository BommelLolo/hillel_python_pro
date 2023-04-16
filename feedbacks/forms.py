from django import forms

from django.core.exceptions import ValidationError
from feedbacks.models import Feedback


class FeedbackModelForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Feedback
        fields = ('user', 'product', 'rating', 'text')

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_name(self):
        try:
            Feedback.objects.get(user=self.cleaned_data['user'])
        except Feedback.DoesNotExist:
            raise ValidationError('User is not sign in! '
                                  'Sign in to send a feedback')
        return self.cleaned_data
