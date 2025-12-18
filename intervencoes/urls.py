from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django.contrib.auth import views as auth_views
from .views import IntervencaoViewSet
from .views import api_intervencoes
from django.urls import reverse_lazy

router = DefaultRouter()
router.register(r'comentarios', views.ComentarioViewSet)
router.register(r'intervencoes', IntervencaoViewSet, basename='intervencoes')

urlpatterns = router.urls

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('cadastro/', views.pagina_cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='logged_out.html'), name='logout'),
    # Somente a API REST
    path('api/', include(router.urls)),
    path("projeto/", views.projeto_view, name="projeto"),
    path('intervencoes/', api_intervencoes, name='api_intervencoes'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='password_reset_form.html',
             success_url=reverse_lazy('password_reset_done')  # 👈 redireciona para a rota correta
         ),
         name='password_reset'),

    path('password_reset_done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password_reset_done.html'
         ),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password_reset_confirm.html'
         ),
         name='password_reset_confirm'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset_complete.html'
         ),
         name='password_reset_complete'),
]
