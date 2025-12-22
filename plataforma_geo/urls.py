from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from intervencoes import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rotas do site (HTML)
    path('', include('intervencoes.urls')),

    # Rotas de autenticação social (Google, etc)
    path('accounts/', include('allauth.urls')),

    # Página específica
    path("analise_dados/", views.analise_dados, name="analise_dados"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
