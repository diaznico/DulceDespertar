from django.db import models

# Create your models here.

class adicionales(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=200)
    imagen=models.ImageField(upload_to='adicionales')
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='adicional'
        verbose_name_plural='adicionales'

    
    def __str__(self):
        return self.titulo