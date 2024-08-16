from django.urls import path
from users import views 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_user ,name='login'), 
    path('logout/', LogoutView.as_view(template_name= 'website/inicio.html'),name='logout'), 
    path('registro/', views.registro,name='registro'),   
    path('editarperfil/', views.editar_perfil,name='editarperfil'),   
    path('cambiar_pass/', views.Cambiar_password.as_view(),name='cambiarpass'), 
    ]
