from django.db import models

# Modelo de Fornecedor (já existente)
class Fornecedor(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome do Fornecedor")
    contato = models.CharField(max_length=100, null=True, blank=True, verbose_name="Pessoa de Contato")
    telefone = models.CharField(max_length=20, null=True, blank=True, verbose_name="Telefone")
    email = models.EmailField(null=True, blank=True, verbose_name="E-mail")

    # Relacionamento: Um fornecedor pode ter várias matérias-primas.
    # O 'cascade="all, delete-orphan"' significa que se um fornecedor for apagado,
    # todas as matérias-primas associadas a ele também serão.
    materias_primas = models.ManyToManyField(
        'MateriaPrima', 
        related_name='fornecedores', 
        blank=True,
        verbose_name="Matérias-Primas Fornecidas"
    )

    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"

    def __str__(self):
        return self.nome

# --- NOVO MODELO ADICIONADO ---
class MateriaPrima(models.Model):
    """
    Este modelo representa uma matéria-prima que a gráfica compra.
    """
    
    UNIDADES_CHOICES = [
        ('m²', 'Metro Quadrado (m²)'),
        ('un', 'Unidade (un)'),
        ('kg', 'Quilograma (kg)'),
        ('L', 'Litro (L)'),
        ('m', 'Metro Linear (m)'),
        ('folha', 'Folha'),
    ]

    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome da Matéria-Prima")
    
    unidade_compra = models.CharField(
        max_length=10, 
        choices=UNIDADES_CHOICES, 
        verbose_name="Unidade de Compra"
    )
    
    custo_unidade = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Custo por Unidade de Compra"
    )

    class Meta:
        verbose_name = "Matéria-Prima"
        verbose_name_plural = "Matérias-Primas"
        ordering = ['nome']

    def __str__(self):
        return f"{self.nome} ({self.get_unidade_compra_display()})"