from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vacinationLocal/', include('vacinationLocal.urls', namespace='vacinationLocal')),
    path('localVacina/', include('localVacina.urls', namespace='localVacina')),
]
