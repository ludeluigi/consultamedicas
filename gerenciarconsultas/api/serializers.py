from rest_framework import serializers
from gerenciarconsultas import models

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Paciente
        fields = '__all__'

class GerenciarConsultasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GerenciarConsultas
        fields = '__all__'


class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Medico
        fields = '__all__'



