from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import TutorialUploadForm
from django.http import HttpResponseRedirect
from . models import *
import os
import unicodedata


toggle='-'

def index(request):     # Home page
    context = {0:0}
    return render(request, "coderdojomobile/index.html", context)

def scratch(request,liv):
    if liv =='L*':
        elenco= Libro.objects.order_by('titolo').filter(genere__descrizione='scratch')
        context = {'titolo_liv':"Scratch - Tutti livelli", 'lista': elenco}
    else:
        elenco= Libro.objects.order_by('titolo').filter(livello=liv,genere__descrizione='scratch')
        context = {'titolo_liv':"Scratch - Livello "+liv[-1:], 'lista': elenco}
    return render(request, "coderdojomobile/libri.html", context)

def python(request, liv):
    if liv =='L*':
        elenco= Libro.objects.order_by('titolo').filter(genere__descrizione='python')
        context = {'titolo_liv':"Python - Tutti livelli", 'lista': elenco}
    else:
        elenco= Libro.objects.order_by('titolo').filter(livello=liv,genere__descrizione='python')
        context = {'titolo_liv':"Python - Livello "+liv[-1:], 'lista': elenco}
    return render(request, "libri.html", context)

def html(request, liv):
    if liv =='L*':
        elenco= Libro.objects.order_by('titolo').filter(genere__descrizione='html')
        context = {'titolo_liv':"HTML - Tutti livelli", 'lista': elenco}
    else:
        elenco= Libro.objects.order_by('titolo').filter(livello=liv,genere__descrizione='html')
        context = {'titolo_liv':"HTML - Livello "+liv[-1:], 'lista': elenco}
    return render(request, "libri.html", context)

def java(request, liv):
    if liv =='L*':
        elenco= Libro.objects.order_by('titolo').filter(genere__descrizione='java')
        context = {'titolo_liv':"Java - Tutti livelli", 'lista': elenco}
    else:
        elenco= Libro.objects.order_by('titolo').filter(livello=liv,genere__descrizione='java')
        context = {'titolo_liv':"Java - Livello "+liv[-1:], 'lista': elenco}
    return render(request, "libri.html", context)

def php(request, liv):
    if liv =='L*':
        elenco= Libro.objects.order_by('titolo').filter(genere__descrizione='php')
        context = {'titolo_liv':"PHP - Tutti livelli", 'lista': elenco}
    else:
        elenco= Libro.objects.order_by('titolo').filter(livello=liv,genere__descrizione='php')
        context = {'titolo_liv':"PHP - Livello "+liv[-1:], 'lista': elenco}
    return render(request, "libri.html", context)

def arduino(request, liv):
    if liv =='L*':
        elenco= Libro.objects.order_by('titolo').filter(genere__descrizione='arduino')
        context = {'titolo_liv':"Arduino - Tutti livelli", 'lista': elenco}
    else:
        elenco= Libro.objects.order_by('titolo').filter(livello=liv,genere__descrizione='arduino')
        context = {'titolo_liv':"Arduino - Livello "+liv[-1:], 'lista': elenco}
    return render(request, "libri.html", context)

# Per compilare il DB

def genDB(request):
    f = open( os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"toolbox/static/toolbox/elenco.txt"), "r")
    titoli = f.readlines()
    f.close()


    elenco=dict()
    cont=0
    for t in titoli:
        if t[0:6]!='elenco':
            elenco[cont] = t[:-5]
            unacard= Libro.objects.order_by('titolo').filter(titolo=elenco[cont])
            if len(unacard)==0:    # il titolo non è ancora in DB
#                CheGenere = Genere(descrizione='scratch')
#                CheAutore = Autore(cognome='Coderdojo', nome='Generico')
                print(Genere.objects.order_by('descrizione').filter(descrizione='scratch')[0],
                      Autore.objects.order_by('cognome').filter(cognome='Coderdojo')[0])
                Card = Libro(titolo=elenco[cont],
                             genere=Genere.objects.order_by('descrizione').filter(descrizione='scratch')[0],
                             autore=Autore.objects.order_by('cognome').filter(cognome='Coderdojo')[0])
                Card.save()
#                print(Card)
            cont+=1
    #elenco=dict()
    #for libro in Libro.objects.all().order_by('titolo'):
    #    elenco[libro.titolo] = libro.posizione
    context = {'file_dict': elenco}
    return render(request, "genDB.html", context)

# Pagina con elenco delle liberatorie
def liberatorie(request, spec):
    global toggle
    toggle='' if toggle=='-' else '-'
    if spec == 'cogn':
        elenco = Liberatoria.objects.all().order_by(toggle+'cognome')
    elif spec == 'nome':
        elenco = Liberatoria.objects.all().order_by(toggle+'nome')
    elif spec == 'cons':
        elenco = Liberatoria.objects.all().order_by(toggle+'consegnata')
    else: 
        elenco = Liberatoria.objects.all().order_by(toggle+'data_di_consegna')

    for libera in elenco:
        libera.consegnata = unicodedata.lookup("HEAVY CHECK MARK") if libera.consegnata== True else " "
    context = {'lista': elenco}
    return render(request, "liberatorieLista.html", context)

def nonraggiungibile(request):
    return HttpResponse("<h2>Sito non raggiungibile. Accesso a internet inesistente")

def softwareDojo(request):
    return render(request, "coderdojomobile/softwareDojo.html")

# Usiamo le categorie definite a db
def sprites(request):
	sprite_categories = SpriteCategory.objects.order_by('sprite_category_name')
	context = {
		'sprite_categories': sprite_categories
	}
	return render(request, 'coderdojomobile/sprites.html', context)

def spritesAlieni(request):
    return render(request, "spritesAlieni.html")

def spriteCategory(request, category_id):
	sprites = Sprite.objects.order_by('sprite_name').filter(spritecategory__id=category_id)
	sprite_images = SpriteImages.objects.all().filter(sprite__in=sprites).order_by('image_order')
	for sprite in sprites:
		sprite.imgs = []
		for image in sprite_images:
			if image.sprite.id == sprite.id:
				sprite.imgs.append(image)
	context = {
		'sprites': sprites,
		'sprite_images' : sprite_images
	}
	return render(request, 'coderdojomobile/spritesInCategory.html', context)


#----------------------------------------------------------------------------------------
# Function usate per prova
def libro(request, id):
    try:
        libro = Libro.objects.get(pk=id)
        return HttpResponse("'%s' di %s, %s<br>" % (libro.titolo, libro.autore, libro.genere))
    except Libro.DoesNotExist:
        return HttpResponse("Codice %s inesistente" % id)

def lista(request):
    elenco=dict()
    for libro in Libro.objects.all().order_by('titolo'):
        elenco[libro.titolo] = libro.posizione
    context = {'file_dict': elenco}
    return render(request, "libriLista.html", context)

