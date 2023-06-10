from django.urls import path, include
from .views import pacientViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'pacientVacines', PacientViewSet)

urlpatterns = [

    path('api/', include(router.urls)), 
]