from django.contrib import admin

from .models import Usuario, Noticia, Edicao, Comentario

class ComentarioInline(admin.TabularInline):
    model = Comentario
    extra = 0

class NoticiaInline(admin.TabularInline):
    model = Noticia
    extra = 0

class EdicaoInline(admin.TabularInline):
    model = Edicao
    extra = 0


class UsuarioAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,    {'fields': ['nome']}),
        (None,    {'fields': ['email']}),
        (None, {'fields': ['senha']}),
        (None, {'fields': ['avatar']}),
        (None, {'fields': ['tipo']}),
    ]
    inlines = [EdicaoInline,NoticiaInline,ComentarioInline]


admin.site.register(Usuario, UsuarioAdmin)
