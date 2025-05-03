from django.urls import path,include
from .views import SignUpView, home
from auth import views


urlpatterns = [
    path("auth/", include("django.contrib.auth.urls")),  
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', home, name='home'),  # URL para la vista de inicio
]