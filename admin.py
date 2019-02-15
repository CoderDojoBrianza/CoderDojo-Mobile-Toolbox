from django.contrib import admin

# Register your models here.
from . import models


class LibroOption(admin.ModelAdmin):
    list_display = ('titolo', 'autore', 'genere', 'livello', 'posizione')


class LiberatoriaOption(admin.ModelAdmin):
    list_display = ('cognome', 'nome', 'consegnata', 'data_di_consegna')


admin.site.register(models.Genere)
admin.site.register(models.Autore)
admin.site.register(models.Libro)
admin.site.register(models.Liberatoria)

admin.site.register(models.Sprite)

admin.site.register(models.SpriteCategory)

admin.site.register(models.SpriteImages)

admin.site.register(models.LearningMaterial)
admin.site.register(models.Event)
admin.site.register(models.Participant)
admin.site.register(models.Ticket)
admin.site.register(models.Rating)
admin.site.register(models.Badge)

admin.site.register(models.OperatingSystem)
admin.site.register(models.SoftwareTool)
admin.site.register(models.LearningTopic)
admin.site.register(models.Waiver)
admin.site.register(models.GenericUserFile)
