from django.utils import timezone


from django.db import models
from django.contrib.auth.models import AbstractUser

# Modelo de Usuario Personalizado
class UsuarioPersonalizado(AbstractUser):
    biografia = models.TextField(blank=True, null=True)

# Modelo de Personaje
class Personaje(models.Model):

    CLASES = [
        ('stalker', 'Stalker'),
        ('mecanico', 'Mecanico'),
        ('ciberchaman', 'Ciberchaman'),
        ('granjero', 'Granjero'),
    ]

    TRAUMA_RESPONSE = [
        ('stalker', 'Cuando entras en panico, todo aliado cercano debe hacer una salvacion de MIEDO'),
        ('mecanico', 'Los jugadores cercanos a ti tienen desventaja en las salvaciones de MIEDO'),
        ('ciberchaman', 'Cuando fallas una salvación de cordura, todos los jugadores cercanos ganan 1 ESTRÉS'),
        ('granjero', 'Una vez por sesion, puedes tener ventaja en un check de PANICO'),
    ]

    nombre = models.CharField(max_length=30)
    usuario = models.ForeignKey(UsuarioPersonalizado, on_delete=models.CASCADE, related_name="personajes")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    clase = models.CharField(max_length=12, choices=CLASES,default='stalker')

    #stats
    fuerza = models.IntegerField()
    velocidad = models.IntegerField()
    intelig = models.IntegerField()
    combat = models.IntegerField()

    #saves
    sanity = models.IntegerField()
    fear = models.IntegerField()
    cuerpo = models.IntegerField()

    #status report
    maxHP = models.IntegerField()
    maxWounds = models.IntegerField(default=2)
    stress = models.IntegerField(default=2)
    traumaRes = models.CharField(max_length=12, choices=TRAUMA_RESPONSE,default='stalker')

    #Equipment
    dinero = models.IntegerField(blank=True)
    armorPoints = models.IntegerField(blank=True)
    extras = models.TextField(max_length=500,blank=True)

    #Override del guardado para modificar los stats que el jugador NO escoge
    def save(self,*args, **kwargs):
        if self.clase == 'stalker':
            self.combat+=10
            self.cuerpo+=10
            self.fear+=20
            self.maxWounds+=1

        if self.clase == 'mecanico':
            #PENDING -10 a un stat
            self.intelig+=20
            self.fear+=60
            self.maxWounds+=1

        if self.clase == 'ciberchaman':
            #PENDING +5 a 1 stat
            self.intelig+=10
            self.sanity+=30

        if self.clase == 'granjero':
            #+5 stats
            self.fuerza+=5
            self.velocidad+=5
            self.intelig+=5
            self.combat+=5
            #+10 saves
            self.sanity+=10
            self.fear+=10
            self.cuerpo+=10

        super(Personaje, self).save(*args, **kwargs)

#Modelo de Armas.
class Arma(models.Model):
    RANGOS = [
        ('short','Short'),
        ('long','Long'),
        ('melee','Melee'),
    ]
    personaje = models.ForeignKey(Personaje,on_delete=models.CASCADE, related_name="armas")
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField(default=10)
    danho = models.TextField(max_length=5)
    crit = models.TextField(max_length=30)
    alcance = models.CharField(max_length=12, choices=RANGOS,default='long')
    tiros = models.IntegerField(blank=True)
    especial = models.TextField(blank=True)
    ammoPrice = models.TextField(blank=True)

