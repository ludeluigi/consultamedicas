"""
URL configuration for consultamedicas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from gerenciarconsultas.api import viewsets as GerenciarConsultasViewSet
from gerenciarconsultas.api import viewsets as PacienteViewSet
from gerenciarconsultas.api import viewsets as MedicoViewSet
from gerenciarconsultas.api.viewsets import GerenciarConsultasViewSet, PacienteViewSet, MedicoViewSet

route = routers.DefaultRouter()

route.register(r'gerenciarconsultas',GerenciarConsultasViewSet, basename= 'gerenciarconsultas')
route.register(r'paciente',PacienteViewSet, basename= 'paciente')
route.register(r'medico',MedicoViewSet, basename= 'medico')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    #path('', GerenciarConsultasViewSet.GerenciarConsultasView.as_view()),

]
