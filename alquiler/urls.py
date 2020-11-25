from django.conf.urls import url
from . import views

urlpatterns = [
    url('alquiler/nuevo/', views.alquiler_nuevo, name='alquiler_nuevo'),
    url('/principal', views.principal, name='principal'),
]
