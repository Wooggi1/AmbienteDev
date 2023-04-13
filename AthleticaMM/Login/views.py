from django.shortcuts import render, HttpResponse

# Create your views here.
def Erro(request):
    return render(request, 'error.html')