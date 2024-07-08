from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from gerenciarconsultas.models import Paciente, Medico, GerenciarConsultas

# Create your tests here.
# arquivos de teste para viewsets

class GerenciarConsultasViewSetTestCase(APITestCase):

    def setUp(self):
        self.paciente = Paciente.objects.create(
            nome="Paciente Teste", profissao="Profissão Teste", telefone="123456789", email="paciente@teste.com", endereco="Endereço Teste"
        )
        self.medico = Medico.objects.create(
            nome="Medico Teste", profissao="Profissão Teste", telefone="123456789", email="medico@teste.com", endereco="Endereço Teste",
            conselho="Conselho Teste", especialidade="Especialidade Teste"
        )
        self.url = reverse('gerenciarconsultas-list')

    def test_list(self):
        consulta1 = GerenciarConsultas.objects.create(
            paciente=self.paciente, medico=self.medico
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)