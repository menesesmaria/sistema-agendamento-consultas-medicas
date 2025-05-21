from django.contrib import admin

from .models import (
    EspecialidadeMedica, EspecialidadeConsulta, PlanoSaude, Paciente, Profissional,
    DisponibilidadeMedico, HorarioDisponivel, Consulta, PacientePlano, ProfissionalPlano
)

admin.site.register([
    EspecialidadeMedica, EspecialidadeConsulta, PlanoSaude, Paciente, Profissional,
    DisponibilidadeMedico, HorarioDisponivel, Consulta, PacientePlano, ProfissionalPlano
])
