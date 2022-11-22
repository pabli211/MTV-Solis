from django.db import models

class Familiar(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    edad= models.IntegerField()
    nacimiento= models.DateField()

    def __str__(self):
        return self.nombre+" "+self.apellido
