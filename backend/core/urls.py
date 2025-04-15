from django.urls import path
from .views import home, wishlist

urlpatterns = [
    path('', home, name='home'),
    path('wishlist/', wishlist, name='wishlist')
]
