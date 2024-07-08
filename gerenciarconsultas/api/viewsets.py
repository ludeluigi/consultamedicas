from rest_framework import viewsets
from gerenciarconsultas.models import GerenciarConsultas, Paciente , Medico
from gerenciarconsultas import models
from gerenciarconsultas.api.serializers import GerenciarConsultasSerializer, PacienteSerializer , MedicoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class PacienteViewSet(viewsets.ModelViewSet):
    serializer_class = PacienteSerializer
    queryset = models.Paciente.objects.all()

class PacienteView(APIView):

    def get(self, request, format=None):
        content = {'user': str(request.user),'auth': str(request.auth)}
        return Response(content)
    

class MedicoViewSet(viewsets.ModelViewSet):
    serializer_class = MedicoSerializer
    queryset = models.Medico.objects.all()

class MedicoView(APIView):

    def get(self, request, format=None):
        content = {'user': str(request.user),'auth': str(request.auth)}
        return Response(content)

class GerenciarConsultasViewSet(viewsets.ModelViewSet):
    serializer_class = GerenciarConsultasSerializer
    queryset = models.GerenciarConsultas.objects.all()

class GerenciarConsultasView(APIView):

    def get(self, request, format=None):
        content = {'user': str(request.user),'auth': str(request.auth)}
        return Response(content)
    



