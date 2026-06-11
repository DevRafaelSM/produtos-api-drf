from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from produtos.models import Produto
from produtos.serializers import ProdutoSerializer


class ProdutoListCreateAPIView(ListCreateAPIView):
    queryset = Produto.objects.all()

    serializer_class = ProdutoSerializer


class ProdutoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()

    serializer_class = ProdutoSerializer
