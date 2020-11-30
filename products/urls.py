from django.urls import path
from .views import ProductListApiView, ProductDetailApiView


urlpatterns = [
    path('', ProductListApiView.as_view()),
    path('<int:pk>/', ProductDetailApiView.as_view()),
]