from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoría')
    nombreCategoria = models.CharField(max_length=50, verbose_name="Nombre de la Categoría")

    def __str__(self):
        return self.nombreCategoria

class Juego(models.Model):
    pegi = models.CharField(max_length=6, primary_key=True, verbose_name="Pegi")
    nombre = models.CharField(max_length=20, verbose_name="Nombre juego")
    precio = models.IntegerField(max_length=20, null=True, blank=True, verbose_name="Precio")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.pegi
    