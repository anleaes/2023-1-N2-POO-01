from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estoque_local/', include('localStorage.urls', namespace='localStorage')),
    path('funcionarios/', include('employee.urls', namespace='employee')),
    path('local_vacinacao/', include('vacinationLocal.urls', namespace='vacinationLocal')),
]