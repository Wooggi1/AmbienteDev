from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .models import Profile

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
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already in use')
                return redirect('pagina de cadastro')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('pagina de cadastro')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('pagina de login')
        else:
            messages.info(request, 'passwords do not match')
            return redirect('pagina de cadastro')
    else:
        return render(request, 'register.html')

def ForgotPassword(request):
    return render(request, 'forgotPassword.html')