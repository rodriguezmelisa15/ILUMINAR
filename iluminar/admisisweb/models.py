from django.db import models

class Articulos(models.Model):
    codart = models.IntegerField(blank=True, null=True)
    ecodart = models.IntegerField()
    proveedor = models.CharField(max_length=3, blank=True, null=True)
    eproveedor = models.IntegerField()
    articulo = models.CharField(max_length=15, blank=True, null=True)
    descrip = models.CharField(max_length=90, blank=True, null=True)
    embalaje = models.CharField(max_length=2, blank=True, null=True)
    color = models.CharField(max_length=2, blank=True, null=True)
    grupo = models.CharField(max_length=12, blank=True, null=True)
    marca = models.CharField(max_length=3, blank=True, null=True)
    poferta = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    precio1 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    precio2 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    precio3 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    precio4 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    oferta = models.IntegerField()
    plpciva = models.IntegerField()
    calcula = models.IntegerField()
    nppedido = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ncpedir = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nodesc = models.IntegerField(blank=True, null=True)
    noutil = models.IntegerField()
    nutil = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    niva = models.DecimalField(max_digits=5, decimal_places=2)
    ncostop = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    ncostov = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    naum = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    ubica = models.CharField(max_length=3, blank=True, null=True)
    fecham = models.DateField()
    activo = models.IntegerField(blank=True, null=True)
    iddiv = models.IntegerField(blank=True, null=True)
    colref = models.IntegerField(blank=True, null=True)
    imagen = models.CharField(max_length=35, blank=True, null=True)
    ldsp = models.IntegerField(blank=True, null=True)
    c002 = models.IntegerField(blank=True, null=True)
    ec002 = models.IntegerField()
    proveedor2 = models.CharField(max_length=3, blank=True, null=True)
    eproveedor2 = models.IntegerField()
    embalaje2 = models.CharField(max_length=2, blank=True, null=True)
    color2 = models.CharField(max_length=2, blank=True, null=True)
    grupo2 = models.CharField(max_length=12, blank=True, null=True)
    marca2 = models.CharField(max_length=3, blank=True, null=True)
    fh = models.DateTimeField()

    class Meta:
        db_table = 'articulos'

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
    idemp = models.CharField(max_length=2)
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
    idusu = models.IntegerField(primary_key=True)
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
