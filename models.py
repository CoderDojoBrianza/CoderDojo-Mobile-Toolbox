from django.db import models


# Create your models here.
class Autore(models.Model):
    nome = models.CharField(max_length=49)
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
    posizione = models.CharField(max_length=200, default="null")

    class Meta:
        verbose_name_plural = "Libri"

    def __str__(self):
        return self.titolo


class Liberatoria(models.Model):
    nome = models.CharField(max_length=30)
    cognome = models.CharField(max_length=30, default="")
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
    file = models.FileField(max_length=200)

    def __str__(self):
        return self.title


class LearningTopic(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1500)
    screenshot = models.FileField(max_length=200, upload_to="learningtopic/")

    def __str__(self):
        return self.title


class LearningMaterial(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1500)
    tutorial = models.OneToOneField(
        GenericUserFile,
        on_delete=models.CASCADE,
        related_name='+',
        null=True
    )
    resources = models.ManyToManyField(
        GenericUserFile,
        related_name='+',
        null=True
    )
    screenshot = models.OneToOneField(
        GenericUserFile,
        on_delete=models.DO_NOTHING,
        related_name='+',
        null=True
    )
    topic = models.ForeignKey(
        LearningTopic,
        on_delete=models.DO_NOTHING,
        null=True
    )
    is_active = models.BooleanField(default=True)
    level = models.IntegerField()

    def __str__(self):
        return self.title


class Badge(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1500)
    image = models.FileField(max_length=200)
    requisites = models.CharField(max_length=3000)

    def __str__(self):
        return self.title


class Participant(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    uuid = models.CharField(max_length=200)
    badges = models.ManyToManyField(Badge, related_name='+', null=True)

    def __str__(self):
        return self.name + " " + self.surname + "(" + self.uuid + ")"


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1500)
    event_date = models.DateField()

    def __str__(self):
        return self.title + "(" + self.event_date.strftime('%d-%B-%Y') + ")"


class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING, null=True)
    participant = models.ForeignKey(
        Participant,
        on_delete=models.DO_NOTHING,
        null=True
    )
    has_checked_in = models.BooleanField(default=False)
    uuid = models.CharField(max_length=1500)

    def __str__(self):
        return self.participant.__str__() + " at " + self.event.__str__()


class Rating(models.Model):
    material = models.ForeignKey(LearningMaterial, on_delete=models.DO_NOTHING)
    value = models.DecimalField(max_digits=3, decimal_places=2)
    rating_date = models.DateField()
    # Max length of IPv6 addr https://bit.ly/2L5VjQA
    rating_source = models.CharField(max_length=45)
    rating_author = models.CharField(max_length=150, null=True, blank=True)
    comment = models.CharField(max_length=1500, null=True, blank=True)

    def __str__(self):
        return "Rating " + str(self.value) + " for "
        + self.material.__str__() + " on " + self.rating_date.__str__()
        + (" by " + self.comment if self.comment is not None else "")


# For software tools
class OperatingSystem(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1500)

    def __str__(self):
        return self.title


class SoftwareTool(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1500)
    operating_systems = models.ManyToManyField(
        OperatingSystem,
        related_name='+'
    )
    executable = models.OneToOneField(
        GenericUserFile,
        on_delete=models.CASCADE,
        related_name='+',
        null=True
    )
    topic = models.ForeignKey(
        LearningTopic,
        on_delete=models.DO_NOTHING,
        null=True
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
