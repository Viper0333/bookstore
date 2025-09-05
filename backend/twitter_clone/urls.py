from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from twitter_clone import views

# Função home
def home(request):
    return HttpResponse("Olá! Este é o Twitter Clone.")

urlpatterns = [
    # Home
    path('', home, name="home"),
    
    # Admin
    path('admin/', admin.site.urls),

    # API Endpoints
    path('api/tweets/', include('tweets.urls')),         # Endpoints de tweets
    path('api/users/', include('users.urls')),           # Endpoints de usuários (cadastro, perfil, etc.)
    path('api/posts/', include('posts.urls')),           # Endpoints de posts (separei de users)

    # JWT para login
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),  # Login
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"), # Refresh token

    # Rotas adicionais
    path("update_server/", views.update, name="update"),
    path("hello/", views.hello_world, name="hello_world"),
]
