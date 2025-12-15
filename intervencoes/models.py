from django.db import models
from django.contrib.auth.models import User

class Intervencao(models.Model):
    CATEGORIAS = [
        ("MOBILIÁRIO URBANO", "MOBILIÁRIO URBANO"),
        ("ESPAÇOS LIVRES DE ESTAR", "ESPAÇOS LIVRES DE ESTAR"),
        ("FESTAS E EVENTOS", "FESTAS E EVENTOS"),
        ("PAISAGISMO", "PAISAGISMO"),
        ("FINALIDADE COMERCIAL", "FINALIDADE COMERCIAL"),
        ("INFRAESTRUTURA URBANA", "INFRAESTRUTURA URBANA"),
    ]
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    descricao = models.TextField()  # Descrição detalhada
    imagem = models.ImageField(upload_to='fotos/', blank=True, null=True)
    latitude = models.FloatField()  # Latitude do ponto
    longitude = models.FloatField()  # Longitude do ponto
    data_registro = models.DateField(auto_now_add=True)  # Data/hora do registro
    usuario = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.categoria} ({self.latitude}, {self.longitude})"


class Comentario(models.Model):
    texto = models.TextField()  # Texto do comentário
    data = models.DateField(auto_now_add=True)  # Data/hora do comentário
    intervencao = models.ForeignKey(
        Intervencao,
        on_delete=models.CASCADE
    )
    usuario = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'Comentário em "{self.intervencao.titulo[:30]}"'



