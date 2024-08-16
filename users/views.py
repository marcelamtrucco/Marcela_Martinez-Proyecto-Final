from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm, UserEditForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


def login_user(request):
    msg_login=''
    if request.method=='POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user= authenticate(request,username=usuario, password=contra)
            if user is not None:
                login(request,user)
                return render(request,'website/inicio.html')                
        msg_login = 'Usuario o contraseña incorrectos'
    form= AuthenticationForm()
    return render (request, 'users/login.html', {'form':form,'msg_login': msg_login })


def registro(request):
    msg_registro=''
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            return render(request,'website/inicio.html')
        msg_registro='Ud ha ingresado datos incorrectos, vuelva a registrarse'
    form= UserRegisterForm()
    return render(request,'users/registro.html',{'form':form, 'mensaje': msg_registro})   

@login_required
def editar_perfil(request):
    usuario=request.user
    if request.method=='POST':
        form = UserEditForm(request.POST, request.FILES, instance= request.user)
        if form.is_valid():
            if form.cleaned_data.get('imagen'):
                usuario.avatar.imagen = form.cleaned_data.get('imagen')
                usuario.avatar.save()                
            form.save()
            return render(request,'website/inicio.html')
    else:    
        form= UserEditForm(initial= {'imagen':usuario.avatar.imagen},instance=request.user)
    return render(request,'users/editar_perfil.html',{'form':form, 'usuario':usuario}) 


class Cambiar_password(LoginRequiredMixin, PasswordChangeView):
    template_name= 'users/cambiar_password.html'
    success_url= reverse_lazy('login')



