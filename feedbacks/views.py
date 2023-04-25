from django.shortcuts import render
from django.views.generic import ListView, CreateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from feedbacks.model_forms import FeedbackModelForm
from feedbacks.models import Feedback


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

    # def get_context_data(self, **kwargs):
    #     kwargs['feedbacks'] = Feedback.objects.iterator()
    #     kwargs.update({'user': self.request.user})
    #     context = super().get_context_data(**kwargs)
    #     # context.update({'form': self.form_class})
    #     return context
    #
    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(data=request.POST)
    #     if form.is_valid():
    #         form.save()
    #     return render(request, 'feedbacks/index.html', context={
    #         'feedback': Feedback.objects.iterator()
    #         # 'form': form
    #     })


class FeedbackList(ListView):
    template_name = 'feedbacks/index.html'
    model = Feedback
