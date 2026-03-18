from django.urls import path
from . import views
urlpatterns = [
    path('get-users/', views.GetUsersView.as_view(), name='get-users'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('verify', views.VerifyEmailView.as_view(), name='verify'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change-password'),
]