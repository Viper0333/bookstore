from django.urls import path
from . import views

urlpatterns = [
    # Página principal do feed (lista de posts)
    path('', views.feed, name='feed'),

    # Criar novo post
    path('novo/', views.novo_post, name='novo_post'),
]
