from django.urls import path, include

from .views import (
    home,
    register,
    PasswordChange,
    PasswordChangeDone,
)
from django.contrib.auth.views import (
    LogoutView,
    LoginView,
)

app_name = 'accounts'

urlpatterns = [
    path('api/', include('accounts.api.urls')),

    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('password/change/', PasswordChange.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDone.as_view(), name='password_change_done'),
]
