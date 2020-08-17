from django.contrib import admin
from .models import Sensores, Valvulas
from rest_basic.models import Article, Valvulas_Water
# Register your models here.

admin.site.register(Sensores)
admin.site.register(Valvulas_Water)
admin.site.register(Article)
admin.site.register(Valvulas)
