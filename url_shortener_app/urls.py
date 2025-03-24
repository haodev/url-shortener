from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('shorten/', views.shorten_url, name='shorten_url'),
    path('original/', views.get_original_url, name='get_original_url'),
    path('redirect/', views.redirect_to_original, name='api_redirect'),
    path('<str:short_code>', views.redirect_in_browswer, name='redirect')
]