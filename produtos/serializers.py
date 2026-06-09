from rest_framework import serializers

from produtos.models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ["nome", "descricao", "preco", "ativo", "criado_em", "atualizado_em"]
        read_only_fields = ["criado_em", "atualizado_em"]
