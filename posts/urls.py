from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed, name='post'),
    path('novo/', views.novo_post, name='novo_post'),
]
