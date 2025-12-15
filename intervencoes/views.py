from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets, permissions
from .models import Intervencao, Comentario
from .serializers import IntervencaoSerializer, ComentarioSerializer
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Intervencao


def pagina_inicial(request):
    return render(request, 'pagina_inicial.html')
# intervencoes/views.py

class IntervencaoViewSet(viewsets.ModelViewSet):
    queryset = Intervencao.objects.all().order_by('-data_registro')
    serializer_class = IntervencaoSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:  # GET liberado
            permission_classes = [permissions.AllowAny]
        else:  # POST, PUT, DELETE só logado
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]


def pagina_cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Nome de usuário já está em uso.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já cadastrado.')
        else:
            user = User.objects.create_user(username=nome, email=email, password=senha)
            user.save()

            # Faz login automático
            user_autenticado = authenticate(username=nome, password=senha)
            if user_autenticado is not None:
                login(request, user_autenticado)
                messages.success(request, 'Cadastro e login realizados com sucesso!')
                return redirect('pagina_inicial')

    return render(request, 'cadastro.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('pagina_inicial')  # ajuste para sua url inicial
        else:
            messages.error(request, 'Usuário ou senha inválidos')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def projeto_view(request):
    return render(request, "projeto.html")

def analise_dados(request):
    return render(request, "analise_dados.html")

class IntervencaoViewSet(viewsets.ModelViewSet):
    queryset = Intervencao.objects.all()
    serializer_class = IntervencaoSerializer
    parser_classes = (MultiPartParser, FormParser)


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

@csrf_exempt
def api_intervencoes(request):
    if request.method == "POST":
        categoria = request.POST.get("categoria")
        descricao = request.POST.get("descricao")
        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")
        imagem = request.FILES.get("imagem")

        # Se você já tiver login no frontend, pode pegar o usuário autenticado
        usuario = request.user if request.user.is_authenticated else None

        # validação mínima
        if not (categoria and descricao and latitude and longitude):
            return JsonResponse({"error": "Campos obrigatórios faltando"}, status=400)

        # cria a intervenção
        intervencao = Intervencao.objects.create(
            categoria=categoria,
            descricao=descricao,
            latitude=float(latitude),
            longitude=float(longitude),
            imagem=imagem,
            usuario=usuario
        )

        return JsonResponse({
            "id": intervencao.id,
            "categoria": intervencao.categoria,
            "descricao": intervencao.descricao,
            "latitude": intervencao.latitude,
            "longitude": intervencao.longitude,
            "imagem": intervencao.imagem.url if intervencao.imagem else None,
            "data_registro": intervencao.data_registro.strftime("%d/%m/%Y"),
            "usuario": intervencao.usuario.username if intervencao.usuario else None
        })

    elif request.method == "GET":
        dados = []
        for i in Intervencao.objects.all().order_by("-data_registro"):
            dados.append({
                "id": i.id,
                "categoria": i.categoria,
                "descricao": i.descricao,
                "latitude": i.latitude,
                "longitude": i.longitude,
                "imagem": i.imagem.url if i.imagem else None,
                "data_registro": i.data_registro.strftime("%d/%m/%Y"),
                "usuario": i.usuario.username if i.usuario else None
            })
        return JsonResponse(dados, safe=False)

    return JsonResponse({"error": "Método não permitido"}, status=405)