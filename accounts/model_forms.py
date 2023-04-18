from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

User = get_user_model()


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)

    def clean_email(self):
        try:
            User.objects.get(email=self.cleaned_data['email'])
        except User.DoesNotExist:
            return self.cleaned_data['email']
        raise ValidationError('User already exist')

    def clean(self):
        self.cleaned_data['username'] = self.cleaned_data[
            'email'
        ].split('@')[0]
        return self.cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
            return user

# not need with the last realization of views

# from django import forms
# from django.contrib.auth import authenticate
# from django.core.exceptions import ValidationError
#
#
# class LoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(
#         widget=forms.PasswordInput()
#     )
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.user = None
#
#     def clean(self):
#         self.user = authenticate(username=self.cleaned_data.get('username'),
#                                  password=self.cleaned_data.get('password'))
#         if self.user is None:
#             raise ValidationError('Error')
#         return self.cleaned_data
