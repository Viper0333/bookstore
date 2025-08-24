from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import MeAPIView, ProfileAPIView

urlpatterns = [
    # endpoint para gerar token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # endpoint para renovar token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # endpoints protegidos
    path('me/', MeAPIView.as_view(), name='api_me'),
    path('profile/', ProfileAPIView.as_view(), name='api_profile'),
]

