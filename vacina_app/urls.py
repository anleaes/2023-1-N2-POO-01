from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estoque_local/', include('localStorage.urls', namespace='localStorage')),
    path('funcionarios/', include('employee.urls', namespace='employee')),
    path('local_vacinacao/', include('vacinationLocal.urls', namespace='vacinationLocal')),
    path('fornecedores/', include('vaccineSupplier.urls', namespace='vaccineSupplier')),
    path('vacinas/', include('vaccines.urls', namespace='vaccines')),
    path('campanhas/', include('campaings.urls', namespace='campaings')),
    path('vacinas_paciente/', include('pacientVacines.url', namespace='pacientVacines')),
    path('pacientes/', include('pacient.urls', namespace='pacients')),
    path('agendamentos_vacinacao/', include('vaccineScheduling.url', namespace='vaccineScheduling')),
]