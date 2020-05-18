from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


@login_required
def home_view(request):
  if request.method == 'POST':
    texto = request.POST['text']
    return redirect('home')

  return render(request,'home/index.html')


@login_required
def about_view(request):
  return render(request,'home/about.html')