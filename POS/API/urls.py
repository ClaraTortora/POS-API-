from django.urls import path
from . import views

urlpatterns = [
    path('categoria', views.CategoriaList.as_view()),
    path('producto', views.ProductoList.as_view()),
]