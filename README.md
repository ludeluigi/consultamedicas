# API de Gerenciamento de Consultas

Este projeto foi desenvolvido em Django para gerenciar consultas médicas

## Funcionalidade

- **Cadastro de Pacientes**: Permite registrar novos pacientes com informações como nome, CPF, data de nascimento e histórico médico.
  
- **Cadastro de Médicos**: Permite registrar novos médicos com informações como nome, CPF, data de nascimento, especialidade e CRM.
  
- **Agendamento de Consultas**: Permite agendar consultas associando pacientes e médicos, especificando data e hora.

- **Edição e Remoção**: Funcionalidades para editar e remover informações de pacientes, médicos e consultas.

## Requisitos do Projeto

O projeto foi desenvolvido utilizando Django, um framework web em Python. Para executar o projeto localmente, siga os passos abaixo:

1. **Instalação do Ambiente Virtual (opcional, mas recomendado)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use venv\Scripts\activate

2. **Instalação das dependências:**:
   pip install -r requirements.txt

3. **Migração do banco de dados:**:
   python manage.py migrate

4. **Iniciar o servidor**:
   python manage.py runserver #Acesse o sistema através do endereço web que será fornecido geralmente

5. **Testes**:
   python manage.py test 


2. **Instalação do Ambiente Virtual (opcional, mas recomendado)**:
