from django.contrib import admin

from .models import (
    Especialidade, PlanoSaude, Cid, Exame, Paciente, Profissional,
    Disponibilidade, Agendamento, PacientePlano, ProfissionalPlano
)

admin.site.register([
    Especialidade, PlanoSaude, Cid, Exame, Paciente, Profissional,
    Disponibilidade, Agendamento, PacientePlano, ProfissionalPlano
])
