from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home, name='home'),  # rota para a raiz /
    # path('api/', include('accounts.urls')),      # todas as rotas de urls.py vão pra /api/
    path('api/', include('accounts.urls_api')),  # todas as rotas de urls_api.py vão pra /api/
    path('', include('accounts.urls')),  # agora homepage é login
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
