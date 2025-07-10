from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome do Fornecedor")
    contato = models.CharField(max_length=100, null=True, blank=True, verbose_name="Pessoa de Contato")
    telefone = models.CharField(max_length=20, null=True, blank=True, verbose_name="Telefone")
    email = models.EmailField(null=True, blank=True, verbose_name="E-mail")

    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"
        ordering = ['nome']

    def __str__(self):
        return self.nome