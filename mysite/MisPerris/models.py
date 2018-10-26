from django.db import models
from django.utils import timezone
#prueba
from django.contrib.auth.models import User


class Post(models.Model):
    
    ESTADO = (
        ('Espera', 'Espera'),
        ('Adoptado', 'Adoptado'),
    )

    Nombre = models.CharField(max_length=100)
    Raza = models.CharField(max_length=100)
    Caracteristicas= models.TextField()
    estado = models.TextField(choices=ESTADO, default='Espera')
    picture = models.ImageField(
        upload_to='user_pics', default='default.jpg')

    def __str__(self):
        return self.Nombre

# Create your models here.

