from django.shortcuts import render

from feedbacks.forms import FeedbackModelForm
from feedbacks.models import Feedback


def feedbacks(request, *args, **kwargs):
    form = FeedbackModelForm
    if request.method == 'POST':
        form = form(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = form()
    context = {
        'feedback': Feedback.objects.iterator(),
        'form': form
    }
    return render(request, 'feedbacks/index.html', context)

# def feedbacks(request, *args, **kwargs):
#     user = request.user
#     form = FeedbackModelForm(user=user)
#     if request.method == 'POST':
#         form = FeedbackModelForm(user=user, data=request.POST)
#         if form.is_valid():
#             form.save()
#     context = {
#         'feedback': Feedback.objects.iterator(),
#         'form': form
#     }
#     return render(request, 'feedbacks/index.html', context)
