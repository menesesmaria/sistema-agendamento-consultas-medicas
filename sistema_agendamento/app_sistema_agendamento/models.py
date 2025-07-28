from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

LETRAS_ALFABETO = [(chr(i), chr(i)) for i in range(ord('A'), ord('Z') + 1)]
NUMEROS_SUBGRUPO = [(i, str(i)) for i in range(1, 22)]
NUMEROS_SUBCATEGORIA = [(i, str(i)) for i in range(0, 10)]

# Create your models here.

class Especialidade(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome
        
class PlanoSaude(models.Model):
    nome = models.CharField("Nome do plano", max_length=100, default="Plano Desconhecido")
    cnpj = models.CharField("CNPJ", max_length=18, null=True, blank=True)
    endereco = models.CharField("Endereço", max_length=200, null=True, blank=True)
    telefone = models.CharField("Telefone de contato", max_length=15, null=True, blank=True)
    razao_social = models.CharField("Razão Social", max_length=150, null=True, blank=True)

    def __str__(self):
        return self.nome


class Cid(models.Model):
    capitulo = models.CharField(
        max_length=1,
        choices=LETRAS_ALFABETO,
        null=True, 
        blank=True)  
    subgrupo = models.IntegerField(
        choices=NUMEROS_SUBGRUPO,
        null=True, 
        blank=True)
    nome = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.capitulo}{self.subgrupo} - {self.nome}"
    
class Exame(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome}"

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
    nome = models.CharField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    data_nascimento = models.DateField
    obs_medicas = models.TextField
    bairro = models.CharField(max_length=30, null=True, blank=True)
    rua = models.CharField(max_length=30, null=True, blank=True)
    numero_residencia = models.IntegerField()
    cep = models.CharField(max_length=8, null=True, blank=True)
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
        null=True, 
        blank=True
    )
    data_nascimento = models.DateField(null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    tempo_experiencia = models.CharField(max_length=15, null=True, blank=True)
    nivel = models.CharField(max_length=50, null=True, blank=True)
    instituicao_formacao = models.CharField(max_length=100, null=True, blank=True)
    especialidades_medicas = models.ManyToManyField(Especialidade)
    bairro = models.CharField(max_length=30)
    rua = models.CharField(max_length=30)
    numero_residencia = models.IntegerField()
    cep = models.CharField(max_length=8)
    cpf = models.CharField(max_length=20)
    crm = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        especialidades = ', '.join([e.nome for e in self.especialidades_medicas.all()])
        return f"{self.nome} - {especialidades} - CRM: {self.crm}"

class Disponibilidade(models.Model):
    profissional = models.ForeignKey('Profissional', on_delete=models.CASCADE)
    data_horario = models.DateTimeField()
    duracao_consulta = models.IntegerField(null=True, blank=True)
    disponivel = models.BooleanField(default=True)
    bloqueado = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.data_horario < timezone.now():
            self.disponivel = False
            self.bloqueado = True
        else:
            self.disponivel = True
            self.bloqueado = False
        super().save(*args, **kwargs)

    def __str__(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        return f"{self.profissional} - {self.data_horario.strftime('%d/%m/%Y %H:%M')} ({status})"

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, null=True)
    profissional = models.ForeignKey(Profissional, on_delete=models.SET_NULL, null=True)

    disponibilidade = models.ForeignKey(
        Disponibilidade,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'disponivel': True, 'bloqueado': False}
    )

    situacao = models.CharField(
        max_length=45,
        choices=Situacao.choices,
        default="Selecionar"
    )
    pagamento = models.CharField(max_length=50, null=True, blank=True)
    plano_saude = models.ForeignKey(PlanoSaude, on_delete=models.SET_NULL, null=True)
    descricao = models.TextField(null=True, blank=True)
    cid = models.ForeignKey(Cid, on_delete=models.SET_NULL, null=True)
    subcategoria = models.IntegerField(
        choices=NUMEROS_SUBCATEGORIA,
        null=True,
        blank=True
    )
    exames_solicitados = models.ForeignKey(Exame, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Consulta de {self.paciente} com {self.profissional} em {self.disponibilidade.data_horario.strftime('%d/%m/%Y %H:%M')}"

    def get_disponibilidades_do_profissional(self):
        """
        Retorna apenas horários disponíveis do profissional específico selecionado.
        """
        if not self.profissional:
            return Disponibilidade.objects.none()

        return Disponibilidade.objects.filter(
            profissional=self.profissional,
            disponivel=True,
            bloqueado=False
        ).distinct()



class PacientePlano(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    plano = models.ForeignKey(PlanoSaude, on_delete=models.CASCADE)
    validade = models.DateField(null=True, blank=True)
    numero_registro = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    bloqueado = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.validade and self.validade < timezone.now().date():
            self.disponivel = False
            self.bloqueado = True
        else:
            self.disponivel = True
            self.bloqueado = False
        super().save(*args, **kwargs)

    class Meta:
        unique_together = (('paciente', 'plano'),)

    def __str__(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        validade_str = self.validade.strftime('%d/%m/%Y') if self.validade else "Sem validade"
        return f"{self.paciente} - {self.plano} ({validade_str}) ({status})"   
    

class ProfissionalPlano(models.Model):
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    plano = models.ForeignKey(PlanoSaude, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.profissional} - {self.plano}"

    class Meta:
        unique_together = (('profissional', 'plano'),)


