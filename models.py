from django.db import models

# Create your models here.
class Autore(models.Model):
    nome= models.CharField(max_length=49)
    cognome = models.CharField(max_length=49)
    class Meta:
        verbose_name_plural = "Autori"
    def __str__(self):
        return "%s %s" % (self.nome, self.cognome)
    
class Genere(models.Model):
    descrizione = models.CharField(max_length=31)
    class Meta:
        verbose_name_plural = "Generi"
    def __str__(self):
        return self.descrizione
    
class Libro(models.Model):
    LIVELLI = (
        ('L1', 'Livello 1'),
        ('L2', 'Livello 2'),
        ('L3', 'Livello 3'))
    titolo = models.CharField(max_length=100)
    autore = models.ForeignKey(Autore, on_delete=models.CASCADE)
    genere = models.ForeignKey(Genere, on_delete=models.CASCADE)
    livello = models.CharField(max_length=2, choices=LIVELLI, default='L1')
    posizione = models.CharField(max_length = 200, default = "null")
    class Meta:
        verbose_name_plural = "Libri"
    def __str__(self):
        return self.titolo
    
class Liberatoria(models.Model):
    nome = models.CharField(max_length=30)
    cognome = models.CharField(max_length=30, default = "")
    consegnata = models.BooleanField()
    data_di_consegna = models.DateField()
    class Meta:
        verbose_name_plural = "Liberatorie"
    def __str__(self):
        return "%s %s" % (self.nome, self.cognome)

    


class Sprite(models.Model):
	sprite_name = models.CharField(max_length=200)


class SpriteCategory(models.Model):
	sprite = models.ManyToManyField(Sprite)
	sprite_category_name = models.CharField(max_length=200)
	sprite_category_description = models.CharField(max_length=500)
	category_image = models.CharField(max_length=500)


class SpriteImages(models.Model):
	sprite = models.ForeignKey(Sprite, on_delete=models.CASCADE)
	image_order = models.IntegerField()
	image_file = models.CharField(max_length=200)


class GenericUserFile(models.Model):
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=1500)
	file_path = models.CharField(max_length=200)


class DojoProject(models.Model):
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=1500)
	tutorial = models.OneToOneField(GenericUserFile, on_delete=models.CASCADE, related_name='+', null=True)
	resources = models.ManyToManyField(GenericUserFile, related_name='+')
	screenshot = models.OneToOneField(GenericUserFile, on_delete=models.DO_NOTHING, related_name='+', null=True)
	