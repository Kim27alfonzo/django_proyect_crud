from django.urls import path
from post.views import PostListView, PostCreateView, PostReadView, PostUpdateView, PostDeleteView

urlpatterns = [

    path('', PostListView.as_view(), name='post_list'),  # URL para la lista de artículos
    path('articulo/create/', PostCreateView.as_view(), name='post_create'),  # URL para crear un nuevo artículo
    path('articulo/read/<int:pk>', PostReadView.as_view(), name='post_read'),  # URL para leer un artículo específico
    path('articulo/read/<int:pk>/update',PostUpdateView.as_view(), name='post_update'),  # URL para actualizar un artículo específico
    path('articulo/read/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),  # URL para eliminar un artículo específico
    path('logout/', PostDeleteView.as_view(), name='post_logout'),  # URL para cerrar sesión (esto debería ser manejado por el sistema de autenticación de Django)
]