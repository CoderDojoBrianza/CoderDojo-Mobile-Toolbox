from django.contrib import admin

# Register your models here.
from .models import *

class LibroOption(admin.ModelAdmin):
    list_display = ( 'titolo', 'autore', 'genere', 'livello', 'posizione')

class LiberatoriaOption(admin.ModelAdmin):
    list_display = ('cognome', 'nome', 'consegnata', 'data_di_consegna')

admin.site.register(Genere)
admin.site.register(Autore)
admin.site.register(Libro, LibroOption)
admin.site.register(Liberatoria, LiberatoriaOption)

admin.site.register(Sprite)

admin.site.register(SpriteCategory)

admin.site.register(SpriteImages)

admin.site.register(GenericUserFile)

admin.site.register(LearningMaterial)
admin.site.register(Event)
admin.site.register(Participant)
admin.site.register(Ticket)