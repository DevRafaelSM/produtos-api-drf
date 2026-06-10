from django.urls import path

from produtos import views

urlpatterns = [
    path(
        "",
        views.ProdutoListCreateAPIView.as_view(),
        name="produto-list-create",
    ),
    path(
        "<int:pk>/",
        views.ProdutoRetrieveUpdateDestroyAPIView.as_view(),
        name="produto-detail",
    ),
]
