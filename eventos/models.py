from django.db import models

# Create your models here.
class Categorias(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)

    class Meta:
        db_table = "Categorias"

class Eventos(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=70)
    fechaInicio = models.DateField(auto_now=False, auto_now_add=False, auto_created=False, null=False)
    fechaFin = models.DateField(auto_now=False, auto_now_add=False, auto_created=False, null=False)
    cantidadAsistentesMaximo = models.IntegerField(null=False)
    estatus = models.BooleanField(null=True, default=False)
    categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT)

    class Meta:
        db_table = "Eventos"

class Participantes(models.Model):

    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=45, null=False, blank=False)
    apellidoPaterno = models.CharField(max_length=45, null=False, blank=False)
    apellidoMaterno = models.CharField(max_length=45, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    evento = models.ForeignKey(Eventos, on_delete=models.PROTECT)

    class Meta:
        db_table = "Participantes"

class Asistencias(models.Model):

    id = models.AutoField(primary_key=True)
    fechaEntrada = models.DateTimeField(auto_now=False, auto_now_add=False, auto_created=False, null=False)
    fechaSalida = models.DateTimeField(auto_now=False, auto_now_add=False, auto_created=False, null=True)
    participante = models.ForeignKey(Participantes, on_delete=models.PROTECT)

    class Meta:
        db_table = "Asistencias"

class Qrs(models.Model):

    id = models.AutoField(primary_key=True)
    # Hay que definir un formato de imágen específico en este campo
    imagen = models.ImageField()
    datos = models.CharField(max_length=100, null=False)
    estatus = models.BooleanField(null=False, default=True)
    evento = models.ForeignKey(Eventos, on_delete=models.PROTECT)

    class Meta:
        db_table = "Qrs"

class QrsParticipantes(models.Model):

    id = models.AutoField(primary_key=True)
    qr = models.ForeignKey(Qrs, on_delete=models.PROTECT)
    participante = models.ForeignKey(Participantes, on_delete=models.PROTECT)

    class Meta:
        db_table = "QrsParticipantes"