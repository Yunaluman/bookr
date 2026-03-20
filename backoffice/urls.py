from django.urls import path
from backoffice import views

app_name = 'backoffice'

urlpatterns = [
    path('', views.index, name='index'),
    # Livres
    path('livres/', views.livres_list, name='livres_list'),
    path('livres/ajouter/', views.livre_create, name='livre_create'),
    path('livres/<int:pk>/modifier/', views.livre_update, name='livre_update'),
    path('livres/<int:pk>/supprimer/', views.livre_delete, name='livre_delete'),
    # Auteurs
    path('auteurs/', views.auteurs_list, name='auteurs_list'),
    path('auteurs/ajouter/', views.auteur_create, name='auteur_create'),
    path('auteurs/<int:pk>/modifier/', views.auteur_update, name='auteur_update'),
    path('auteurs/<int:pk>/supprimer/', views.auteur_delete, name='auteur_delete'),
]
