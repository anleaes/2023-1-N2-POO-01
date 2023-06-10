from django.urls import include, path
from rest_framework import routers
from .views import VacinationLocalViewSet

router = routers.DefaultRouter()
router.register(r'VacinationLocal', VacinationLocalViewSet)

urlpatterns = [
    # Outras rotas da sua aplicação
    path('api/', include(router.urls)),
]