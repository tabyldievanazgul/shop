from django.urls import path
from .views import WishlistAddApiView

urlpatterns = [
    path('', WishlistAddApiView.as_view()),
    # path('cabinet/', WishlistApiView.as_view())
]