from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('sign-in/', views.sign_in, name='sign_in'),
]
