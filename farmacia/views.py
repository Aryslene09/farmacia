from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Pedido
from .forms import ProdutoForm, PedidoForm


def home(request):
    return render(request, 'farmacia/home.html')


def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'farmacia/lista_produtos.html', {'produtos': produtos})


def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'farmacia/form_produto.html', {'form': form})


def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'farmacia/form_produto.html', {'form': form})


def apagar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('lista_produtos')


def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'farmacia/lista_pedidos.html', {'pedidos': pedidos})


def criar_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'farmacia/form_pedido.html', {'form': form})


def editar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'farmacia/form_pedido.html', {'form': form})


def apagar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    pedido.delete()
    return redirect('lista_pedidos')
