from django.shortcuts import render

# from feedbacks.forms import FeedbackModelForm
# from feedbacks.models import Feedback


def feedbacks(request, *args, **kwargs):

    # form = FeedbackModelForm
    # if request.method == 'POST':
    #     form = form(data=request.POST)
    #     if form.is_valid():
    #         form.save()
    # else:
    #     form = form()
    # feedback_list = Feedback.objects.iterator()
    return render(request, 'feedbacks/index.html')
    # return render(request, 'feedbacks/index.html', context={
    #     'feedback': feedback_list,
    #     'form': form
    # })
