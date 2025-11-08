from django.contrib import admin

from .models import (
    Estado, Cidade, Bairro, Logradouro, Especialidade, PlanoSaude, Cid, Exame, Paciente, Profissional,
    Disponibilidade, Agendamento, Consulta, PacientePlano, ProfissionalPlano
)

admin.site.register([
     Estado, Cidade, Bairro, Logradouro, Especialidade, PlanoSaude, Cid, Exame, Paciente, Profissional,
    Disponibilidade, Agendamento, Consulta, PacientePlano, ProfissionalPlano
])
