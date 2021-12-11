from django.db import models

# Create your models here.

class desayunos(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=200)
    imagen=models.ImageField(upload_to='desayunos')

    descripcion=models.TextField(max_length=500)

    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='desayuno'
        verbose_name_plural='desayunos'

    
    def __str__(self):
        return self.titulo

