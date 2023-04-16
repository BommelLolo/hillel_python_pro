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
