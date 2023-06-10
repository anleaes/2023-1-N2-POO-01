from django.urls import include, path
from rest_framework import routers
from .views import EmployeeViewSet

router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet)

urlpatterns = [
    # Outras rotas da sua aplicação
    path('api/', include(router.urls)),
]