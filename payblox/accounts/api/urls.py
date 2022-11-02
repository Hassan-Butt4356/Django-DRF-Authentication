from django.urls import path, include
from .views import (
    UserRegistrationView,
    UserLoginView,
    UserChangePasswordView,
    SendPasswordResetEmailView,
    UserPasswordResetView,
)
from rest_framework_simplejwt.views import (
    TokenVerifyView,
    TokenRefreshView,
    TokenObtainPairView
)

app_name = 'accounts'

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='registeration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('gettoken/', TokenObtainPairView.as_view(), name='get-token'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='refresh-token'),
    path('verifytoken/', TokenVerifyView.as_view(), name='verify-token'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
]
