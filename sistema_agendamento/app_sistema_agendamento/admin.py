from django.contrib import admin

from .models import (
    Especialidade, PlanoSaude, Paciente, Profissional,
    Disponibilidade, Consulta, PacientePlano, ProfissionalPlano
)

admin.site.register([
    Especialidade, PlanoSaude, Paciente, Profissional,
    Disponibilidade, Consulta, PacientePlano, ProfissionalPlano
])
