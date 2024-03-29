from django import forms

from feedbacks.models import Feedback


class FeedbackModelForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('text', 'user', 'rating')

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget = forms.HiddenInput()
        self.fields['user'].initial = user
        self.fields['rating'].help_text = "Rating should be from 1 to 5."
