from django.core.mail import mail_admins
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from django.utils.translation import gettext_lazy as _

from main.forms import ContactForm
from project.celery import send_email_task


class MainView(TemplateView):
    template_name = 'main/index.html'


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contacts/index.html'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        # django can send html-messages instead common messages
        msg = f'FROM: ' \
              f'{form.cleaned_data["email"]}\n{form.cleaned_data["text"]}'
        text = _('Contact form')
        send_email_task.apply_async((text, msg), retry=False)
        return super().form_valid(form)
