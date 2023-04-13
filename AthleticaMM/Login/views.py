from django.shortcuts import render, HttpResponse

# Create your views here.
def Erro(request):
    return render(request, 'error.html')

def Logado(request):
    return render(request, 'sucess.html')

def PaginaLogin(request):
    return render(request, 'index.html')