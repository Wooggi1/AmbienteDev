from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

# Create your views here.

class Index(View):
    def get(self, request):
        return render(request, 'index.html')

def Erro(request):
    return render(request, 'error.html')

def Logado(request):
    return render(request, 'sucess.html')

def PaginaLogin(request):
    return render(request, 'index.html')

def Register(request):
    return render(request, 'register.html')

def ForgotPassword(request):
    return render(request, 'forgotPassword.html')