from django.urls import path
from post.views import PostListView, PostCreateView

urlpatterns = [

    path('', PostListView.as_view(), name='post_list'),  # URL para la lista de artículos
    path('create/', PostCreateView.as_view(), name='post_create'),  # URL para crear un nuevo artículo
]