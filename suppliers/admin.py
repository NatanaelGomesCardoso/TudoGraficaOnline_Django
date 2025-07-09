from django.contrib import admin
from .models import Fornecedor # Importa o nosso modelo Fornecedor

# Register your models here.

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    """
    Esta classe personaliza como o modelo Fornecedor é exibido
    na área administrativa do Django.
    """
    
    # Define quais colunas aparecerão na lista de fornecedores.
    list_display = ('id', 'nome', 'contato', 'telefone', 'email')
    
    # Adiciona um campo de pesquisa no topo da lista.
    # Permite pesquisar por nome, contato ou e-mail.
    search_fields = ('nome', 'contato', 'email')
    
    # Adiciona um filtro na lateral direita para facilitar a busca.
    # (Será mais útil quando tivermos mais campos, como 'estado' ou 'cidade').
    list_filter = ('nome',)
    
    # Define a ordem padrão da lista (pelo nome, em ordem alfabética).
    ordering = ('nome',)