from django.contrib import admin
from django.urls import path
from app_GlobalTalentConnect import views

urlpatterns = [
    path('/', views.usuarios_home, name="home"),
    path('cadastro/', views.cadastro, name="cadastro"),
    path('usuarios/', views.usuarios_home, name="usuarios"),
    path('exclusao/<int:id_usuario>', views.excluir_usuario, name='excluir_usuario'),
    path('excluir/', views.exclusao, name="aba_excluir"),
]

