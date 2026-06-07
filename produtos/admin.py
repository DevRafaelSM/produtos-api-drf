from django.contrib import admin

from produtos.models import Produto


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "ativo", "criado_em", "atualizado_em")
    search_fields = ["nome"]
    list_filter = ["ativo"]


admin.site.register(Produto, ProdutoAdmin)
