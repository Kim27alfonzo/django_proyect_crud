from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Articulo
from django.views.generic import ListView
from django.views.generic import DetailView
from django.urls import reverse_lazy
# Create your views here.

class PostListView (ListView):
    template_name = 'post_list.html'
    model = Articulo
    context_object_name = 'lista'  # Nombre del contexto para la lista de artículos
    


class PostCreateView(CreateView):
    template_name = 'post_create.html'
    model = Articulo
    fields = ['titulo', 'descripcion', 'imagen', 'author']  # Campos del formulario
    context_object_name = 'create' # Nombre del contexto para el formulario
    success_url = reverse_lazy("post_list")  # URL de redirección después de crear el artículo

class PostReadView (DetailView):
    template_name = 'post_read.html'
    model = Articulo
    context_object_name = 'read'  # Nombre del contexto para el artículo
    fields = ['titulo', 'descripcion', 'imagen', 'author']  # Campos del formulario
    success_url = reverse_lazy("post_list")  # URL de redirección después de crear el artículo