from django.db import models

# Create your models here.

class EspecialidadeMedica(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)

class EspecialidadeConsulta(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)

class PlanoSaude(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)

class Paciente(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    obs_medicas = models.TextField(null=True, blank=True)
    bairro = models.CharField(max_length=30)
    rua = models.CharField(max_length=30)
    numero_residencia = models.IntegerField()
    cep = models.CharField(max_length=8)
    sexo = models.CharField(max_length=5)

class Profissional(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    sexo = models.CharField(max_length=5, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    tempo_experiencia = models.CharField(max_length=15, null=True, blank=True)
    nivel = models.CharField(max_length=50, null=True, blank=True)
    instituicao_formacao = models.CharField(max_length=100, null=True, blank=True)
    especialidade_medica = models.ForeignKey(EspecialidadeMedica, on_delete=models.SET_NULL, null=True)
    bairro = models.CharField(max_length=30)
    rua = models.CharField(max_length=30)
    numero_residencia = models.IntegerField()
    cep = models.CharField(max_length=8)
    cpf = models.CharField(max_length=20)

class DisponibilidadeMedico(models.Model):
    DIAS_SEMANA = [
        ('Segunda', 'Segunda'),
        ('Terça', 'Terça'),
        ('Quarta', 'Quarta'),
        ('Quinta', 'Quinta'),
        ('Sexta', 'Sexta'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo'),
    ]
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=10, choices=DIAS_SEMANA)
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()
    duracao_consulta = models.IntegerField()
    ativo = models.BooleanField(default=True)

class HorarioDisponivel(models.Model):
    disponibilidade = models.ForeignKey(DisponibilidadeMedico, on_delete=models.CASCADE)
    data_horario = models.DateTimeField()
    disponivel = models.BooleanField(default=True)
    bloqueado = models.BooleanField(default=False)

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, null=True)
    profissional = models.ForeignKey(Profissional, on_delete=models.SET_NULL, null=True)
    especialidade_consulta = models.ForeignKey(EspecialidadeConsulta, on_delete=models.SET_NULL, null=True)
    horario = models.ForeignKey(HorarioDisponivel, on_delete=models.SET_NULL, null=True)
    data = models.DateField(null=True, blank=True)
    horario_consulta = models.TimeField(null=True, blank=True)
    duracao_estimada = models.IntegerField(null=True, blank=True)
    duracao_final = models.IntegerField(null=True, blank=True)
    situacao = models.CharField(max_length=50, null=True, blank=True)
    pagamento = models.CharField(max_length=50, null=True, blank=True)
    convenio = models.CharField(max_length=100, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    prescricao = models.TextField(null=True, blank=True)
    diagnostico = models.TextField(null=True, blank=True)
    exames_solicitados = models.TextField(null=True, blank=True)

class PacientePlano(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    plano = models.ForeignKey(PlanoSaude, on_delete=models.CASCADE)
    validade = models.DateField(null=True, blank=True)
    numero_registro = models.IntegerField()

    class Meta:
        unique_together = (('paciente', 'plano'),)

class ProfissionalPlano(models.Model):
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    plano = models.ForeignKey(PlanoSaude, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('profissional', 'plano'),)
