from django.urls import path
from .views import create_short_url, redirect_to_url

urlpatterns = [
    path('shorten/', create_short_url, name='shorten_url'),
    path('<str:shortcode>/', redirect_to_url, name='retrieve_url'),
]