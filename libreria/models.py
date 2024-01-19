from django.db import models

# Create your models here.
class Libro(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=100,verbose_name='Titulo')
    imagen=models.ImageField(upload_to='imagenes/',verbose_name='Image',null=True)
    descripcion=models.TextField(verbose_name='Descripcion',null=True)

    def __str__(self):
        fila="Titulo "+self.titulo+"-"+"Descripción: "+self.descripcion
        return fila
    
# esta funcion es para eliminar la imagen
    def delete(self,using=None,keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()