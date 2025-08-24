from django.urls import path
from . import views
from .views import UserListView

urlpatterns = [
    path('register/', views.RegisterAPIView.as_view(), name='api_register'),
    path('me/', views.MeAPIView.as_view(), name='api_me'),
    path('profile/', views.ProfileAPIView.as_view(), name='api_profile'),
    path('follow/<str:username>/', views.FollowAPIView.as_view(), name='api_follow'),
    path('feed/', views.FeedAPIView.as_view(), name='api_feed'),
    path('users/', UserListView.as_view(), name='user-list'),

    # Interações
    path('posts/<int:post_id>/like/', views.LikeAPIView.as_view(), name='post-like'),
    path('posts/<int:post_id>/comment/', views.CommentAPIView.as_view(), name='post-comment'),
]


