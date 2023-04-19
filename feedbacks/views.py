from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import render

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
        context.update({'form': self.form_class})
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'feedbacks/index.html', context={
            'feedback': Feedback.objects.iterator(),
            'form': form
        })

    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)
