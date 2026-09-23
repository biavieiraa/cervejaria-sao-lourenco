from django.db import models
from django.contrib.auth.models import User

class Produto(models.Model):
    CATEGORIAS = (
        ('CERVEJA', 'Cerveja em Garrafa/Lata'),
        ('CHOPP', 'Barril de Chopp'),
    )
    nome = models.CharField(max_length=150)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='CERVEJA')
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0)
    descricao = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)

    def __str__(self):
        return f"{self.nome} - R$ {self.preco} (Estoque: {self.estoque})"

class Pedido(models.Model):
    STATUS_CHOICES = (
        ('PENDENTE', 'Aguardando Pagamento'),
        ('PAGO', 'Pagamento Confirmado'),
        ('CANCELADO', 'Cancelado'),
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDENTE')
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pagamento = models.CharField(max_length=50)

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario.username} - {self.status}"