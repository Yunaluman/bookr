from django.urls import path
from bookr_app import views

app_name = 'bookr_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('auteurs/', views.auteurs_list, name='auteurs_list'),
    path('auteurs/<int:auteur_id>/', views.auteur_detail, name='auteur_detail'),
]
