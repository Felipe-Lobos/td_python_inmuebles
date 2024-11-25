"""
URL configuration for proyecto_inmuebles project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from gestion_inmuebles.views import registro, pagina_principal, profile, inmuebles,inmuebles_detalle, inmuebles_agregar, inmuebles_actualizar,inmuebles_eliminar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',pagina_principal, name='inicio'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('registro/',registro, name='register'),
    path('profile/',profile,name='profile'),
    path('inmuebles/',inmuebles,name='inmuebles'),
    path('inmuebles/agregar/',inmuebles_agregar,name='inmuebles_agregar'),
    path('inmuebles/<int:id_inmueble>',inmuebles_detalle,name='inmuebles_detalle'),
    path('inmuebles/<int:id_inmueble>/actualizar',inmuebles_actualizar,name='inmuebles_actualizar'),
    path('inmuebles/<int:id_inmueble>/eliminar',inmuebles_eliminar,name='inmuebles_eliminar'),
]