from django.urls import path
from django.contrib.auth.decorators import login_required

from feedbacks.views import FeedbackView

urlpatterns = [
    path('', login_required(FeedbackView.as_view()), name='feedbacks')
]
