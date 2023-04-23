from django.urls import path
from django.urls import include

from accounts.views import RegistrationView

# from accounts.views import LoginView, LogoutView

urlpatterns = [
    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout')

    # with this auth we don't need our urls and views
    path('', include('django.contrib.auth.urls')),
    path('signup/', RegistrationView.as_view(), name='signup')
]
