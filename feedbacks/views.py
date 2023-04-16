from feedbacks.model_forms import FeedbackModelForm
from django.views.generic import FormView
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required


class FeedbackView(FormView):
    form_class = FeedbackModelForm
    template_name = 'feedbacks/index.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

# from django.shortcuts import render
# from feedbacks.models import Feedback
#
# @login_required
# def feedbacks(request, *args, **kwargs):
#     user = request.user
#     form = FeedbackModelForm(user=user)
#     if request.method == 'POST':
#         form = FeedbackModelForm(user=user, data=request.POST)
#         if form.is_valid():
#             form.save()
#     context = {
#         'feedbacks': Feedback.objects.iterator(),
#         'form': form
#     }
#     return render(request, 'feedbacks/index.html', context)
