from django.urls import path
from website import views 
from website.views import crear_reserva, list_clases_reservadas,editar_clases_reservadas, eliminar_clases_reservadas

urlpatterns = [
    path('', views.inicio,name='inicio'),
    path('about', views.about,name='about'),
    path('clase/', views.clase,name='clase'),
    path('entrenador/', views.entrenador,name='entrenador'),
    path('alta_socio/', views.alta_socio,name='alta_socio'),  
    path('horarios/', views.horarios,name='horarios'), 
    path('reserva_clase/', crear_reserva.as_view(),name= 'reserva'), 
    path('listar_reserva/', list_clases_reservadas.as_view(),name= 'listar'), 
    path('editar_reserva/<pk>/', editar_clases_reservadas.as_view(),name= 'editar'), 
    path('eliminar_reserva/<pk>/', eliminar_clases_reservadas.as_view(),name= 'eliminar'), 
    path('buscar_clase/', views.buscar,name='buscar_clase'), 
    path('buscar/', views.buscar),   
    path('yoga/', views.list_poses,name='yoga'), 
    path('yogapose/', views.yogapose,name='yogapose'),    
    ]
