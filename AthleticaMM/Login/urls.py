from django.contrib import admin
from django.urls import path, include
from . import views
from .views import Index

urlpatterns = [
    path('logado/', views.Logado, name='logado'),
    path('erro/', views.Erro, name='pagina de erro'),
    path('registro/', views.Register, name='pagina de cadastro'),
    path('EsqueciSenha/', views.ForgotPassword, name='esqueci a senha'),
    path('', Index.as_view(), name='pagina de login'),
]