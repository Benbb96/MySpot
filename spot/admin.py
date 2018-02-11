from django.contrib import admin
from .models import Groupe, Spotteur, Spot, Photo

@admin.register(Groupe)
class GroupeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'created_date', 'modified_date')
    search_fields = ('nom',)

@admin.register(Spotteur)
class SpotteurAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_date', 'modified_date')
    list_filter = ('groupes', )
    search_fields = ('user__username', 'user__first_name', 'user__last_name')

@admin.register(Spot)
class SpotAdmin(admin.ModelAdmin):
    list_display = ('nom','spotteur', 'created_date', 'modified_date')
    list_filter = ('spotteur__user__username', 'groupes_de_partage__nom')
    search_fields = ('nom',)
    ordering = ('nom',)
    date_hierarchy = 'created_date'

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('spot', 'auteur', 'description', 'created_date', 'modified_date')
    search_fields = ('spot__nom', 'auteur__user__username')
