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
        fields = ["id", "nome", "descricao", "preco", "ativo", "criado_em", "atualizado_em"]
        read_only_fields = ["criado_em", "atualizado_em"]
        extra_kwargs = {
            "nome": {
                "error_messages": {
                    "blank": 'O nome do produto não pode ser vazio',
                    "required": 'O nome do produto é obrigatorio',
                    "max_length": 'O nome do produto não pode ultrapassar 100 caracteres'
                }
            },
            "descricao": {
                "error_messages": {
                    "max_length": 'A descrição do produto não pode ultrapassar 1000 caracteres'
                }
            },
            "preco": {
                "error_messages": {
                    "blank": 'O preço do produto não pode ser vazio',
                    "required": 'O preço do produto é obrigatorio',
                }
            }
        }
