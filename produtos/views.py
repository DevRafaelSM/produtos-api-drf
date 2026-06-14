from django.http import Http404
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from produtos.models import Produto
from produtos.serializers import ProdutoSerializer


class ProdutoListCreateAPIView(ListCreateAPIView):
    queryset = Produto.objects.all()

    serializer_class = ProdutoSerializer


class ProdutoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()

    serializer_class = ProdutoSerializer

    def get_object(self):
        try:
            obj = super().get_object()
            return obj
        except (NotFound, Http404):
            raise NotFound(detail={'detail': 'Produto não encontrado.'})

    def perform_destroy(self, instance):
        if not instance.ativo:
            raise ValidationError("Esse produto já encontra-se inativo.")
        else:
            instance.ativo = False
            instance.save()
