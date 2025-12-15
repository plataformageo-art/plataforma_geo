from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from intervencoes import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('intervencoes.urls')),

    # Inclui as URLs do allauth para login social e conta
    path('accounts/', include('allauth.urls')),
    
    
    path('', include('intervencoes.urls')),
    # Inclui as URLs padrões do Django auth (login, logout, reset senha etc)
    # Caso tenha conflito, remova esta linha, mas aí deve ajustar templates e URLs
    #path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name="pagina_inicial.html"), name="home"),
    path("analise_dados/", views.analise_dados, name="analise_dados"),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
