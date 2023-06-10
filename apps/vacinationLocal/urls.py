from django.urls import include, path
from rest_framework import routers
from .views import LocalVacinaViewSet

router = routers.DefaultRouter()
router.register(r'localvacina', LocalVacinaViewSet)

urlpatterns = [
    # Outras rotas da sua aplicação
    path('api/', include(router.urls)),
]