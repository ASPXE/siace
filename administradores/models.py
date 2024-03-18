from django.db import models

# Create your models here.

class Administradores(models.Model):

    id = models.AutoField(primary_key=True)
    administrador = models.CharField(max_length=45)
    nombreAdministrador = models.CharField(max_length=30, null=False, blank=False)
    contrasenia = models.CharField(max_length=300, null=False, blank=False)

    class Meta:
        db_table = "Adimistradores"