from django.db import models

# Create your models here.
#tabla en la base de datos
class ProfesionalCV (models.Model):
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    email= models.EmailField(max_length=200)
    carrera= models.CharField(max_length=200)
    celular = models.CharField(max_length=200)