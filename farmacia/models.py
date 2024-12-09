from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField()
    quantidade_estoque = models.IntegerField()

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    cliente_nome = models.CharField(max_length=100)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)
    data_pedido = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=50, choices=[('Pendente', 'Pendente'), ('Concluído', 'Concluído')], default='Pendente'
    )
    
    def __str__(self):
        return f"{self.cliente_nome} - {self.produto.nome} - {self.status}"

