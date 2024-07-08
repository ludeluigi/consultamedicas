from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    profissao = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    endereco = models.CharField(max_length=300)

    class Meta:
        abstract = True

    def __srt__(self):
        return self.nome
    
class Paciente(Pessoa):
    def __str__(self):
        return self.nome
    

class Medico(Pessoa):
    conselho = models.CharField(max_length=20)
    especialidade = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome} - Especialidade: {self.especialidade} - {self.profissao} - Conselho: {self.conselho}"

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)
    medico = models.ForeignKey(Medico, on_delete=models.DO_NOTHING)
    data = models.DateTimeField(auto_now_add=True)

class GerenciarConsultas(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)
    medico = models.ForeignKey(Medico, on_delete=models.DO_NOTHING)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.data} - {self.paciente} com {self.medico}"







