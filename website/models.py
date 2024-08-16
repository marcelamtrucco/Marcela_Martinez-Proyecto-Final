from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date, datetime

class Clase(models.Model):
    nombre=models.CharField(max_length=30)   #ej. yoga, spinning,etc
    codigo=models.CharField(max_length=20) #codigo identificando clase,dia,horario, ej. yoga, lunes en la mañana sera yo_lu_ma
    
    def __str__(self):
        return f'{self.nombre}'
    
class Entrenador(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    telefono=models.CharField(max_length=50,default='')

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
class Socio(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    telefono=models.CharField(max_length=50)
    id_socio=models.PositiveIntegerField(default= '12345')

    def __str__(self):
        return f'{self.nombre} {self.apellido}'  



class Reserva_Clase(models.Model):
    TIMEBLOCK_CHOICES = (
         ("Yoga_Lu_Mañana", "Yoga_Lunes_ 10:00AM - 11:30AM"),
         ("Yoga_Mar_Tarde", "Yoga_Martes_ 2:00PM - 3:30PM"),
         ("Pilates_Jue_Tarde", "Pilates_Jueves_ 2:00PM - 3:30PM"),
         ("Pilates_Vie_Mañana", "Pilates_Viernes_ 10:00AM - 11:30AM"),
         ("Zumba_Lu_Tarde", "Zumba_Lunes_ 2:00PM - 3:30PM"),
         ("Zumba_Mar_Mañana", "Zumba_Martes_ 10:00AM - 11:30AM"),
         ("Spinning_Mie_Mañana", "Spinning_Miércoles_ 10:00AM - 11:30AM"),
         ("Spinning_Vie_Tarde", "Spinning_Viernes_ 2:00PM - 3:30PM"),  
         ( "Musculación_Mie_Mañana", "Musculación_Miércoles_ 10:00AM - 11:30AM"),
         ("Musculación_Jue_Tarde", "Musculación_Jueves_ 2:00PM - 3:30PM"),              
     )
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    id_socio = models.ForeignKey(Socio, on_delete=models.CASCADE,default= '12345')
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE,default= '')
    turno = models.CharField(max_length=50, choices=TIMEBLOCK_CHOICES, default="----")
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.id_socio}{self.turno}' 
    
class Yoga(models.Model):
    name = models.CharField(max_length=50, blank = True, null = True)
    description = models.CharField(max_length=500, blank = True, null = True)
    benefit = models.CharField(max_length=500, blank = True, null = True)
    image_url = models.CharField( max_length=95, blank = True, null = True)
    
    def __str__(self):
        return f'{self.name}'

