# intervencoes/serializers.py

from rest_framework import serializers
from .models import Intervencao, Comentario

class IntervencaoSerializer(serializers.ModelSerializer):
    categoria_display = serializers.CharField(source='get_categoria_display', read_only=True)
    imagem = serializers.ImageField(max_length=None, use_url=True)
    data_registro = serializers.DateField(format="%Y-%m-%d")  # <-- aqui forçamos só a data

    class Meta:
        model = Intervencao
        fields = ['id', 'descricao', 'latitude', 'longitude', 'categoria', 'categoria_display', 'imagem', 'data_registro']


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'




