from django.urls import reverse
from random import randint

from feedbacks.models import Feedback


def test_feedback_list(client, login_client, feedback_factory, faker):
    for _ in range((randint(3, 20))):
        feedback_factory()
    url = reverse('feedbacks')
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.context['feedbacks']) == Feedback.objects.count()
