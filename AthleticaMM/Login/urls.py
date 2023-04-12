from django.contrib import admin
from django.urls import path, include
from Login.views import Erro, Register, ForgotPassword, Logado, PaginaLogin


urlpatterns = [
    path('logado/', Logado, name='logado'),
    path('erro/', Erro, name='pagina de erro'),
    path('registro/', Register, name='pagina de cadastro'),
    path('EsqueciSenha/', ForgotPassword, name='esqueci a senha'),
    path('login/', PaginaLogin, name='pagina de login')
]