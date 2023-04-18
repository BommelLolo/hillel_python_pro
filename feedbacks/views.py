from django.views.generic import FormView
from django.urls import reverse_lazy

from feedbacks.model_forms import FeedbackModelForm
from feedbacks.models import Feedback


class FeedbackView(FormView):
    form_class = FeedbackModelForm
    template_name = 'feedbacks/index.html'
    success_url = reverse_lazy('feedbacks')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs['feedbacks'] = Feedback.objects.iterator()
        context = super().get_context_data(**kwargs)
        return context

    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)
