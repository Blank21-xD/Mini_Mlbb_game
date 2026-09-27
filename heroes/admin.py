from django.contrib import admin
from .models import Hero


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "base_attack", "base_hp")
    search_fields = ("name", "role")
