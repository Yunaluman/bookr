# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Auteur, Product, ProductItem, Livre, LivreType, LivreStatus


@admin.register(Auteur)
class AuteurAdmin(admin.ModelAdmin):
    list_display = ['prenom', 'nom', 'nationalite', 'nb_livres']
    search_fields = ['nom', 'prenom']
    ordering = ['nom', 'prenom']

    @admin.display(description='Nb livres')
    def nb_livres(self, obj):
        return obj.livres.count()


@admin.register(LivreType)
class LivreTypeAdmin(admin.ModelAdmin):
    list_display = ['genre']
    search_fields = ['genre']


@admin.register(LivreStatus)
class LivreStatusAdmin(admin.ModelAdmin):
    list_display = ['status']
    search_fields = ['status']


@admin.register(Livre)
class LivreAdmin(admin.ModelAdmin):
    list_display = ['nom', 'auteur', 'prix', 'livre_type', 'livre_status']
    list_filter = ['livre_type', 'livre_status', 'auteur']
    search_fields = ['nom', 'auteur__nom', 'auteur__prenom']
    ordering = ['nom']
    fieldsets = (
        ('Informations principales', {'fields': ('nom', 'auteur', 'prix')}),
        ('Classification', {'fields': ('livre_type', 'livre_status')}),
    )


admin.site.register(Product)
admin.site.register(ProductItem)
