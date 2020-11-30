from django.urls import path
from .views import CategoryListApiView, CategoryDetailApiView


urlpatterns =[
    path('catigories/', CategoryListApiView.as_view()),
    path('catigories/<int:pk>/', CategoryDetailApiView.as_view()),

]