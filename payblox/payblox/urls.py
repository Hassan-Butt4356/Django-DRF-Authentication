from django.contrib import admin
from django.urls import path,include

from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls',namespace='accounts')),

    # Password Reset Urls
    path('password_reset/', PasswordResetView.as_view(template_name='accounts/passwordreset.html'),
         name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='accounts/passwordresetdone.html'),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='accounts/passwordresetconfirm.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/',
         PasswordResetCompleteView.as_view(template_name='accounts/passwordresetcomplete.html'),
         name='password_reset_complete'),
]
