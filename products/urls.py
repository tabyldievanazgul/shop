from django.urls import path
from .views import ProductListApiView, ProductDetailApiView, ImageListApiView


urlpatterns = [
    path('', ProductListApiView.as_view()),
    path('<int:pk>/', ProductDetailApiView.as_view()),
    path('images/', ImageListApiView.as_view()),
]