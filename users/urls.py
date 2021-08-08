from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterApiView.as_view()),
    path('activate/<uuid:activation_code>/', views.ActivationView.as_view(), name='activation'),
    path('login/', views.LoginApiView.as_view()),
    path('logout/', views.LogoutView.as_view(), name='auth_logout'),
]