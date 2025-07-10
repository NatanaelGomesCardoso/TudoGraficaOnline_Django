from django.db import models
from suppliers.models import Fornecedor

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome da Categoria")
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['nome']
    def __str__(self):
        return self.nome

class MateriaPrima(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome da Matéria-Prima")
    fornecedores = models.ManyToManyField(Fornecedor, blank=True, verbose_name="Fornecedores")
    class Meta:
        verbose_name = "Matéria-Prima"
        verbose_name_plural = "Matérias-Primas"
        ordering = ['nome']
    def __str__(self):
        return self.nome