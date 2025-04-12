from django.urls import path
from post.views import PostListView, PostCreateView, PostReadView

urlpatterns = [

    path('', PostListView.as_view(), name='post_list'),  # URL para la lista de artículos
    path('create/', PostCreateView.as_view(), name='post_create'),  # URL para crear un nuevo artículo
    path('read/<int:pk>', PostReadView.as_view(), name='post_read'),  # URL para leer un artículo específico
]