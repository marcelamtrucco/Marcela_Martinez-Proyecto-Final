from django.shortcuts import render
from .models import Clase,Entrenador,Socio,Reserva_Clase, Yoga
from django.contrib.auth.models import User
from website.forms import SociosFormulario, Reserva_Form, YogaForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
import requests

def inicio(request):
    return render(request,'website/inicio.html',{})

def about(request):
    return render(request,'website/about.html',{})

def clase(request):
    return render(request,'website/clases.html',{})

def entrenador(request):
    return render(request,'website/entrenadores.html',{})

# funcion para generar un formulario, que permita ingresar nuevos socios a la BD y luego recuperar esa informacion por POST  
def alta_socio(request):
    if request.method=='POST':
        formulario = SociosFormulario(request.POST)
        if formulario.is_valid():
            info_formulario=formulario.cleaned_data
            socio=Socio(nombre=info_formulario['nombre'],apellido=info_formulario['apellido'], email=info_formulario['email'],telefono=info_formulario['telefono'])
            socio.save()
            return render(request,'website/inicio.html')
    else:
        formulario = SociosFormulario()       
    return render(request,'website/socios.html',{'formulario':formulario})  

def horarios(request):
    return render(request,'website/horarios.html',{})

def buscar_clase(request):
   return render(request,'website/inicio.html')

def buscar(request):
    if request.GET['nombre']:
       nombre=request.GET['nombre']
       clases=Clase.objects.filter(nombre__icontains=nombre)
       return render(request,'website/busqueda_clase.html',{'clases':clases,'nombre':nombre})
    else:
        respuesta=f"No se encontraron datos"
    return HttpResponse(respuesta) 

class crear_reserva(LoginRequiredMixin,CreateView):
    form_class= Reserva_Form 
    template_name= 'website/crear_reserva.html'
    success_url=reverse_lazy('reserva')

class list_clases_reservadas(LoginRequiredMixin,ListView):
    model=Reserva_Clase
    template_name='website/lista_reservas.html'
    success_url=reverse_lazy('listar')
    
    def get_queryset(self, *args, **kwargs):
     return Reserva_Clase.objects.all().filter(user=self.request.user)
    
class editar_clases_reservadas(LoginRequiredMixin,UpdateView):
    model= Reserva_Clase
    template_name= 'website/editar_reservas.html'
    fields=['user','clase','turno']
    success_url=reverse_lazy('listar')

class eliminar_clases_reservadas(LoginRequiredMixin,DeleteView):
    model=Reserva_Clase
    template_name='website/eliminar_reservas.html'
    success_url=reverse_lazy('inicio')

# def get_poses(request):
#         poses = {}
#         # if 'name' in request.GET:
#         #     name = request.GET['name']
#         url = 'https://yoga-api-nzy4.onrender.com/v1/poses?'
#         response = requests.get(url)
#         poses = response.json()
#         for i in poses:
#             poses_data = Yoga(name = i['english_name'],description = i['pose_description'],benefit = i['pose_benefits'],image_url = i['url_png'])
#             poses_data.save()
#         poses = Yoga.objects.all()
#         return render (request, 'website/yogaposes.html', {'poses':poses} )

def list_poses(request):
    poses=Yoga.objects.all()
    return render(request, 'website/yogaposes.html',{'poses':poses})

def yogapose(request):
    if request.GET['yoga_pose']:
       nombre=request.GET['yoga_pose']
       poses=Yoga.objects.all()
       return render(request,'website/yoga.html',{'poses':poses,'nombre':nombre})
    else:
        respuesta=f"No se encontraron datos"
    return HttpResponse(respuesta)


