# app_sistema_agendamento/models.py
from django.db import models
class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    # Adicione outros campos conforme necessário
    
    class Meta:
        db_table = 'paciente'
        managed = False

class Agendamento(models.Model):
    id_consulta = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, db_column='id_paciente')
    data = models.DateField()
    horario = models.TimeField()
    # Adicione outros campos conforme sua tabela 'consulta' no BD
    
    class Meta:
        db_table = 'consulta'
        managed = False

    def __str__(self):
        return self.nome