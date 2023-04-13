from django.shortcuts import render, HttpResponse

def Register(request):
    return render(request, 'register.html')

def ForgotPassword(request):
    return render(request, 'forgotPassword.html')