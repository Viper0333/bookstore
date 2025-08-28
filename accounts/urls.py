from django.urls import path
from . import views_html
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('login')),  # raiz redireciona para login
    # Páginas HTML
    path('login/', views_html.login_view, name='login'),
    path('register/', views_html.register_view, name='register'),
    path('profile/', views_html.profile_view, name='profile'),
]



# from django.urls import path
# from . import views, views_html
# from .views import UserListView
# from django.shortcuts import redirect

# def redirect_to_login(request):
#     return redirect('login')

# urlpatterns = [
#     path('', redirect_to_login),  # raiz redireciona pro login
#     path('register/', views.RegisterAPIView.as_view(), name='api_register'),
#     path('me/', views.MeAPIView.as_view(), name='api_me'),
#     path('profile/', views.ProfileAPIView.as_view(), name='api_profile'),
#     path('follow/<str:username>/', views.FollowAPIView.as_view(), name='api_follow'),
#     path('feed/', views.FeedAPIView.as_view(), name='api_feed'),
#     path('users/', UserListView.as_view(), name='user-list'),

#     # Interações
#     path('posts/<int:post_id>/like/', views.LikeAPIView.as_view(), name='post-like'),
#     path('posts/<int:post_id>/comment/', views.CommentAPIView.as_view(), name='post-comment'),
    
#     # Páginas HTML
#     path('login/', views_html.login_view, name='login'),
#     path('register/', views_html.register_view, name='register'),
#     path('profile/', views_html.profile_view, name='profile'),
# ]


