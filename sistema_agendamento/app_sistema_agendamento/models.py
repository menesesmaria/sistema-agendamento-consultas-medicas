# app_sistema_agendamento/models.py
from django.db import models

class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True, db_column='ID_PACIENTE')
    nome = models.CharField(max_length=100, db_column='NOME')
    telefone = models.CharField(max_length=15, db_column='TELEFONE', blank=True, null=True)
    email = models.EmailField(max_length=100, db_column='EMAIL', blank=True, null=True)
    cpf = models.CharField(max_length=14, db_column='CPF', blank=True, null=True)
    data_nascimento = models.DateField(db_column='DATA_NASCIMENTO', blank=True, null=True)
    obs_medicas = models.TextField(db_column='OBS_MEDICAS', blank=True, null=True)
    bairro = models.CharField(max_length=30, db_column='BAIRRO')
    rua = models.CharField(max_length=30, db_column='RUA')
    numero_residencia = models.IntegerField(db_column='NUMERO_RESIDENCIA')
    cep = models.CharField(max_length=8, db_column='CEP')
    sexo = models.CharField(max_length=5, db_column='SEXO')
    
    class Meta:
        db_table = 'paciente'
        managed = False

    def __str__(self):
        return self.nome

class Agendamento(models.Model):  # <-- Certifique-se que esta classe existe
    id_consulta = models.AutoField(primary_key=True, db_column='ID_CONSULTA')
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, db_column='ID_PACIENTE')
    data = models.DateField(db_column='DATA')
    horario = models.TimeField(db_column='HORARIO')
    
    class Meta:
        db_table = 'consulta'
        managed = False

    def __str__(self):
        return f"Agendamento {self.id_consulta} - {self.data}"