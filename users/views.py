
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.db.utils import IntegrityError



"""SignUp"""
def signup(request):
  if request.method == 'POST':
    email = request.POST['email']
    password = request.POST['password']
    password_confirmation = request.POST['password_confirmation']
    if password != password_confirmation:
      return render(request,'users/signup.html',{'error':'La contraseña de confirmación no coincide'})

    try:
      user = User.objects.create_user(password=password,email=email,username=email)
    except IntegrityError:
      return render(request,'users/signup.html',{'error':'Correo ya esta siendo usado'})
      
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.save()
   
    return redirect('login')
  else:
    return render(request,'users/signup.html')


def login_view(request):
  """Login View"""
  if request.method == 'POST':
    username = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user:
      login(request,user)
      return redirect('home')
    else:
      return render(request,'users/login.html',{'error':'Correo o contraseña invalidos'})
    

  return render(request,'users/login.html')


@login_required
def logout_view(request):
  logout(request)
  return redirect('login')