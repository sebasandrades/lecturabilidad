"""lectura URL Configuration
    Punto de entrada del projecto
    Aquí se declaran las rutas que resolverá el servidor de Django
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render

def login(request):
    return render(request,'users/login.html',)
def signup(request):
    return render(request,'users/signup.html',)

urlpatterns = [
    path('users/login/', login,name='login'),
    path('users/signup/', signup,name='signup'),
]
