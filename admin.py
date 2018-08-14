from django.contrib import admin

# Register your models here.
from . import models


class LibroOption(admin.ModelAdmin):
    list_display = ('titolo', 'autore', 'genere', 'livello', 'posizione')


class LiberatoriaOption(admin.ModelAdmin):
    list_display = ('cognome', 'nome', 'consegnata', 'data_di_consegna')


admin.site.register(models.Genere)
admin.site.register(models.Autore)
admin.site.register(models.Libro, LibroOption)
admin.site.register(models.Liberatoria, LiberatoriaOption)

admin.site.register(models.Sprite)

admin.site.register(models.SpriteCategory)

admin.site.register(models.SpriteImages)

admin.site.register(models.GenericUserFile)

admin.site.register(models.LearningMaterial)
admin.site.register(models.Event)
admin.site.register(models.Participant)
admin.site.register(models.Ticket)
