from django.urls import path

from produtos import views

urlpatterns = [
    path(
        "produtos/",
        views.ProdutoListCreateAPIView.as_view(),
        name="produto-list-create",
    ),
    path(
        "produtos/<int:pk>/",
        views.ProdutoRetrieveUpdateDestroyAPIView.as_view(),
        name="produto-detail",
    ),
]
