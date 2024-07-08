from django.test import TestCase
from .models import Paciente, Medico, Consulta
from django.core.exceptions import ValidationError

class ModelsTestCase(TestCase):
    def setUp(self):
        self.paciente = Paciente.objects.create(
            nome="Josefa", cpf="12345678901", data_nascimento="1500-05-20", historico=""
        )
        self.medico = Medico.objects.create(
            nome="Dr. Silva", cpf="98765432100", data_nascimento="1970-11-11", especialidade="Cardiologia", crm="123456"
        )

    def test_paciente_cpf_invalido(self):
        with self.assertRaises(ValidationError):
            paciente_invalido = Paciente(
                nome="João", cpf="123", data_nascimento="1990-01-01"
            )
            paciente_invalido.full_clean()  # Valida o modelo

    def test_medico_crm_invalido(self):
        with self.assertRaises(ValidationError):
            medico_invalido = Medico(
                nome="Dr. Silva", cpf="98765432100", data_nascimento="1970-11-11", especialidade="Cardiologia", crm=""
            )
            medico_invalido.full_clean()  # Valida o modelo

    def test_agendar_consulta_sem_paciente(self):
        with self.assertRaises(ValidationError):
            consulta_invalida = Consulta(
                paciente=None, medico=self.medico, data="2024-07-10 10:00", descricao="Consulta de rotina"
            )
            consulta_invalida.full_clean()  # Valida o modelo

    def test_agendar_consulta_data_invalida(self):
        with self.assertRaises(ValueError):
            Consulta.objects.create(
                paciente=self.paciente, medico=self.medico, data="data-invalida", descricao="Consulta de rotina"
            )

    def test_listar_consultas_vazio(self):
        consultas = Consulta.objects.all()
        self.assertEqual(consultas.count(), 0, "A lista de consultas deve estar vazia")
