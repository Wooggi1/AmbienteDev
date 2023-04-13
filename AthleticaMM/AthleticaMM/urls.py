"""
URL configuration for AthleticaMM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Login.views import Erro
from Login.views import Logado, PaginaLogin
from Register.views import Register, ForgotPassword

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Logado, name='logado'),
    path('erro/', Erro, name='pagina de erro'),
    path('registro/', Register, name='pagina de cadastro'),
    path('EsqueciSenha/', ForgotPassword, name='esqueci a senha'),
    path('login/', PaginaLogin, name='pagina de login')
]
