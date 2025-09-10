from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from twitter_clone import views
from django.conf.urls.static import static
from django.conf import settings

# Função home
def home(request):
    return HttpResponse("Olá! Este é o Twitter Clone.")

urlpatterns = [
    path('', home, name="home"),
    path('admin/', admin.site.urls),

    # Endpoints corretos
    path('api/tweets/', include('tweets.urls')),
    path('api/users/', include('users.urls')),

    # JWT endpoints
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # Extras
    path("update_server/", views.update, name="update"),
    path("hello/", views.hello_world, name="hello_world"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
