from django.db import models

# Create your models here.

class Sensores(models.Model):
    nombre=models.CharField(max_length=50)
    mensaje=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='sensores', blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='sensor'
        verbose_name_plural='sensores'
    
    def __str__(self):
        return self.nombre



class Valvulas(models.Model):

    name=models.CharField(max_length=30,default="")
    state=models.BooleanField(default=False)
    codeStateON=models.CharField(max_length=6)
    codeStateOFF=models.CharField(max_length=6)
