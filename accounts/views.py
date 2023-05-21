from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView as AuthLoginView
from django.urls import reverse_lazy
from django.views.generic import FormView, UpdateView
from django.utils.translation import gettext_lazy as _

from accounts.forms import RegistrationForm, AuthenticationForm, \
    ProfileModelForm


class RegistrationView(FormView):
    template_name = 'registration/signup.html'
    form_class = RegistrationForm
    success_url = settings.LOGOUT_REDIRECT_URL

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        """Security check complete. Sign the user in."""
        messages.success(self.request, _('You has signed successfully in!'))
        return super().form_valid(form)


class LoginView(AuthLoginView):
    form_class = AuthenticationForm

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        messages.success(self.request, _('Welcome back!'))
        return super().form_valid(form)


class ProfileView(FormView):
    form_class = ProfileModelForm
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        return super().form_valid(form)


class PhoneCheckView(UpdateView):
    success_url = reverse_lazy('phone_check')
