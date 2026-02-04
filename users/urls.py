from django.urls import path
from . import views
urlpatterns = [
    path('register', views.RegisterView.as_view(), name='register'),
    path('verify', views.VerifyEmailView.as_view(), name='verify'),
    path('login', views.LoginUser.as_view(), name='login'),

]