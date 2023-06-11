from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('funcionarios/', include('employee.urls', namespace='employee')),
    path('vacinationLocal/', include('vacinationLocal.urls', namespace='vacinationLocal')),
    path('localVacina/', include('localVacina.urls', namespace='localVacina')),
    path('estoque_local/', include('localStorage.urls', namespace='localStorage')),
]