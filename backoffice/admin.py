# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Product, ProductItem, Livre, LivreType, LivreStatus


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
    list_display = ['nom', 'prix', 'livre_type', 'livre_status']
    list_filter = ['livre_type', 'livre_status']
    search_fields = ['nom']
    ordering = ['nom']

    fieldsets = (
        ('Informations principales', {
            'fields': ('nom', 'prix')
        }),
        ('Classification', {
            'fields': ('livre_type', 'livre_status')
        }),
    )


admin.site.register(Product)
admin.site.register(ProductItem)