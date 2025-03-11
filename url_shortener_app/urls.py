from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('shorten/', views.shorten_url, name='shorten_url'),
    path('original/', views.get_original_url, name='get_original_url'),
    path('redirect/', views.redirect_to_original, name='redirect_to_original'),
]