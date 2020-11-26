from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url('alquiler/nuevo/', views.alquiler_nuevo, name='alquiler_nuevo'),
    path('alquiler/lista/', views.alquiler_lista, name='alquiler_lista'),
    path('alquiler/<int:pk>/', views.alquiler_detalle, name='alquiler_detalle'),
    url('', views.principal, name='principal'),
]
