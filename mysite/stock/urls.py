from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='stock-home'),
    path('us-stock/', views.usStock, name='stock-us'),
]
