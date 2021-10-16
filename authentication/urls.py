from django.urls import path

from rest_framework_simplejwt.views import (TokenRefreshView)


from authentication import views

urlpatterns = [
    path("users/<int:id>/", views.UserListView.as_view(), name="users"),
    path("users/", views.AuthUserView.as_view(), name="auth-users"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("verify-email/", views.VerifyEmail.as_view(), name="verify-email"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("token-refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("request-reset-email/", views.RequestResetPasswordEmailView.as_view(),
         name="request-reset-email"),
    path("password-reset/<uidb64>/<token>/", views.PasswordTokenCheckView.as_view(),
         name="password-reset-confirm"),
    path("password-reset-complete/", views.SetNewPasswordView.as_view(),
         name="password-reset-complete"),
    path("change-password/", views.ChangePasswordView.as_view(),
         name="change-password"),
]
