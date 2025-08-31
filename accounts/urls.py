from django.urls import path
from django.shortcuts import redirect
from . import views_html
from . import views  # importa todas as views do app
from .views import criar_profiles_usuarios

urlpatterns = [
    path('', lambda request: redirect('login')),  # raiz redireciona para login
    path('login/', views_html.login_view, name='login'),
    path('register/', views_html.register_view, name='register'),
    path('profile/<str:username>/', views_html.profile_view, name='profile'),
    path("logout/", views_html.logout_view, name="logout"),
    
    # nova rota para posts
    path("posts/", views_html.posts_view, name="posts"),

    # rotas auxiliares
    path('limpar-profiles/', views.limpar_profiles, name='limpar_profiles'),
    path('criar-profiles/', criar_profiles_usuarios, name='criar_profiles'),
]
