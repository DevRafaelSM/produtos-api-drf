from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from rest_framework import serializers

from produtos.models import Produto


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            name="Cadastro de produto",
            value={
                "nome": "Teclado",
                "preco": "5.00",
                "descricao": "Teclado com switches azuis",
                "ativo": True,
            },
            request_only=True,
        )
    ]
)
class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ["nome", "descricao", "preco", "ativo", "criado_em", "atualizado_em"]
        read_only_fields = ["criado_em", "atualizado_em"]
