from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from feedbacks.model_forms import FeedbackModelForm
from feedbacks.models import Feedback
from project.celery import debug_task


class FeedbackView(CreateView):
    form_class = FeedbackModelForm
    template_name = 'feedbacks/create.html'
    success_url = reverse_lazy('feedbacks')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class FeedbackList(ListView):
    template_name = 'feedbacks/index.html'
    model = Feedback

    def get(self, request, *args, **kwargs):
        debug_task.apply_async((2, 6), retry=True, retry_policy={
            'max_retries': 3,
            'interval_start': 0,
            'interval_step': 0.2,
            'interval_max': 0.2,
        })
        return super().get(request, *args, **kwargs)
