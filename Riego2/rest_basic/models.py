from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    mensaje = models.CharField(max_length=100)
    estado=models.BooleanField(default=False)

    def __str__(self):
        return self.title



class Valvulas_Water(models.Model):

    name=models.CharField(max_length=30,default="")
    state=models.BooleanField(default=False)
    codeStateON=models.CharField(max_length=6)
    codeStateOFF=models.CharField(max_length=6)

    def __str__(self):
        return self.title



class Mensaje_Valvulas(models.Model):

    name=models.CharField(max_length=30,default="")

    def __str__(self):
        return self.title