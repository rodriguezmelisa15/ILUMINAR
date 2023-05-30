from django.db import models

class Empresas(models.Model):
    razonsoc = models.CharField(max_length=30)
    fantasia = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    provincia = models.CharField(max_length=15)
    localidad = models.CharField(max_length=20)
    cpostal = models.CharField(max_length=4)
    cpa = models.CharField(max_length=8)
    cuit = models.CharField(max_length=13)
    cm = models.CharField(max_length=14)
    cativa = models.CharField(max_length=1)
    compro = models.CharField(max_length=1)
    fecini = models.DateField()
    telefono = models.CharField(db_column='Telefono', max_length=30)  # Field name made lowercase.
    email = models.CharField(max_length=30)
    web = models.CharField(max_length=30)
    deniva = models.CharField(max_length=25)
    cate = models.CharField(max_length=1)
    sucursal = models.CharField(max_length=3)
    smtpserver = models.CharField(max_length=30)
    sendpassword = models.CharField(max_length=20)
    central = models.IntegerField()
    eslogan = models.CharField(max_length=50)
    idemp = models.CharField(primary_key=True, max_length=2)

    class Meta:
        db_table = 'empresas'


class Sucursales(models.Model):
    sucursal = models.CharField(max_length=3)
    direccion = models.CharField(max_length=30)
    provincia = models.CharField(max_length=15)
    localidad = models.CharField(max_length=20)
    comentario = models.TextField()
    cpa = models.CharField(max_length=8)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    central = models.IntegerField()
    activo = models.IntegerField()
    esucursal = models.IntegerField()
    fh = models.DateTimeField()

    class Meta:
        db_table = 'sucursales'



class Usuarios(models.Model):
    idusu = models.IntegerField()
    usuario = models.CharField(max_length=20)
    passd = models.CharField(max_length=40)
    fechap = models.DateField()
    area = models.CharField(max_length=2)
    secc = models.IntegerField()
    nivel = models.IntegerField()
    idemp = models.CharField(max_length=2)
    fh = models.DateTimeField()

    class Meta:
        db_table = 'usuarios'
