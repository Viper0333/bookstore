import debug_toolbar
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework.authtoken.views import obtain_auth_token
from django.http import HttpResponse

# Swagger imports
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# DRF Routers
from rest_framework.routers import DefaultRouter
from product.views import ProductViewSet, CategoryViewSet
from order.views import OrderViewSet

# View simples para a página inicial
def home(request):
    return HttpResponse("Bem-vindo à Bookstore API!")

# Configuração do Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Bookstore API",
        default_version='v1',
        description="Documentação da API da Bookstore",
        contact=openapi.Contact(email="contato@bookstore.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Configuração do Router
router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'order', OrderViewSet, basename='order')

urlpatterns = [
    # Debug toolbar
    path("__debug__/", include(debug_toolbar.urls)),

    # Admin
    path("admin/", admin.site.urls),

    # Página inicial
    path("", home, name="home"),

    # Autenticação via token
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),

    # Rotas via Router
    path("api/", include(router.urls)),

    # Swagger URLs
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
