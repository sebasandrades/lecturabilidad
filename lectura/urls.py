"""lectura URL Configuration
    Punto de entrada del projecto
    Aquí se declaran las rutas que resolverá el servidor de Django
"""
# Importacion de Django
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

# Proyecto
from users import views as userViews
from lectura import views as lectura_views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/login/', userViews.login_view,name='login'),
    path('users/signup/', userViews.signup,name='signup'),
    path('users/logout/', userViews.logout_view,name='logout'),
    path('', lectura_views.home_view,name='home'),
    path('about/', lectura_views.about_view,name='about'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
