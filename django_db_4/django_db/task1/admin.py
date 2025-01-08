from django.contrib import admin
from .models import *
@admin.register(Bayer)
class BayerAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = ('name', 'balance', 'age')
    list_filter = ('balance', 'age')
    search_fields = ('name',)
    readonly_fields = ('balance',)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('title', 'description', 'cost')
    list_filter = ('cost',)
    search_fields = ('title',)