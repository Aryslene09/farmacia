from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('produtos/', views.lista_produtos, name="lista_produtos"),
    path('produtos/criar/', views.criar_produto, name="criar_produto"),
    path('produtos/<int:id>/editar/', views.editar_produto, name="editar_produto"),
    path('produtos/<int:id>/apagar/', views.apagar_produto, name="apagar_produto"),
    path('pedidos/', views.lista_pedidos, name="lista_pedidos"),
    path('pedidos/criar/', views.criar_pedido, name="criar_pedido"),
    path('pedidos/<int:id>/editar/', views.editar_pedido, name="editar_pedido"),
    path('pedidos/<int:id>/apagar/', views.apagar_pedido, name="apagar_pedido"),
]
