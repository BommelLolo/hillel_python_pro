from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts.views import RegistrationView, LoginView, ProfileView, PhoneCheckView

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', RegistrationView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('id<int:user_id>/', ProfileView.as_view(), name='profile'),
    # path('profile/', ProfileView.as_view(), name='profile'),
    path('phone_check/', PhoneCheckView.as_view(), name='phone_check'),
]
