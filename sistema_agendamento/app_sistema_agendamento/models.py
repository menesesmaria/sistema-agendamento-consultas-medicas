from django.db import models

# Create your models here.

class Especialidade(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome 

class PlanoSaude(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nome 

class Sexo(models.TextChoices):
    masculino = 'Masculino'
    feminino = 'Feminino'
    outro = 'Outro'

class Situacao(models.TextChoices):
    emergencia = 'Emergência - Atendimento imediato'
    muito_urgente = 'Muito urgente - Atendimento em até 10 minutos'
    urgente = 'Urgente - Atendimento em até 60 minutos'
    pouco_urgente = 'Pouco urgente - Atendimento em até 2 horas'
    nao_urgente = 'Não urgente - Atendimento em até 4 horas'

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField
    obs_medicas = models.TextField
    bairro = models.CharField(max_length=30)
    rua = models.CharField(max_length=30)
    numero_residencia = models.IntegerField()
    cep = models.CharField(max_length=8)
    sexo = models.CharField(
        max_length=10,
        choices=Sexo.choices,
    )

    def __str__(self):
        return f"{self.nome} - CPF: {self.cpf}"

class Profissional(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    sexo = models.CharField(
        max_length=10,
        choices=Sexo.choices,
    )
    data_nascimento = models.DateField(null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    tempo_experiencia = models.CharField(max_length=15, null=True, blank=True)
    nivel = models.CharField(max_length=50, null=True, blank=True)
    instituicao_formacao = models.CharField(max_length=100, null=True, blank=True)
    especialidade_medica1 = models.ForeignKey(Especialidade, on_delete=models.SET_NULL, null=True)
    especialidade_medica2 = models.ForeignKey(Especialidade, on_delete=models.SET_NULL, null=True)
    bairro = models.CharField(max_length=30)
    rua = models.CharField(max_length=30)
    numero_residencia = models.IntegerField()
    cep = models.CharField(max_length=8)
    cpf = models.CharField(max_length=20)
    crm = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.nome} - {self.especialidade_medica1} - CRM: {self.crm}"

class Disponibilidade(models.Model):
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    data_horario = models.DateTimeField()
    duracao_consulta = models.IntegerField(null=True, blank=True)
    disponivel = models.BooleanField(default=True)
    bloqueado = models.BooleanField(default=False)

    def __str__(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        return f"{self.profissional} - {self.data_horario.strftime('%d/%m/%Y %H:%M')} ({status})"

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, null=True)
    profissional = models.ForeignKey(Profissional, on_delete=models.SET_NULL, null=True)
    disponibilidade = models.ForeignKey(Disponibilidade, on_delete=models.SET_NULL, null=True, blank=True)
    situacao = models.CharField(
        max_length=45,
        choices=Situacao.choices,
    )
    pagamento = models.CharField(max_length=50, null=True, blank=True)
    plano_saude = models.ForeignKey(PlanoSaude, on_delete=models.SET_NULL, null=True)
    descricao = models.TextField(null=True, blank=True)
    prescricao = models.TextField(null=True, blank=True)
    diagnostico = models.TextField(null=True, blank=True)
    exames_solicitados = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Consulta de {self.paciente} com {self.profissional} em {self.disponibilidade.data_horario.strftime('%d/%m/%Y %H:%M')}"

class PacientePlano(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    plano = models.ForeignKey(PlanoSaude, on_delete=models.CASCADE)
    validade = models.DateField(null=True, blank=True)
    numero_registro = models.IntegerField()

    class Meta:
        unique_together = (('paciente', 'plano'),)

    def __str__(self):
        return f"{self.paciente} - {self.plano}"

class ProfissionalPlano(models.Model):
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    plano = models.ForeignKey(PlanoSaude, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.profissional} - {self.plano}"

    class Meta:
        unique_together = (('profissional', 'plano'),)


