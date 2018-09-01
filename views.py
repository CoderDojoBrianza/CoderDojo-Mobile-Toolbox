from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
# from django.template import loader
# from .forms import TutorialUploadForm
from .forms import CheckInOutForm
# from django.http import HttpResponseRedirect
from . models import Event
from . models import Ticket
from . models import Libro
from . models import Genere
from . models import Autore
from . models import Participant
from . models import SpriteImages
from . models import Sprite
from . models import SpriteCategory
from . models import Liberatoria
from . models import LearningTopic
from . models import OperatingSystem
from . models import SoftwareTool

import os
import unicodedata
from django.contrib.auth.decorators import permission_required

# https://docs.djangoproject.com/en/dev/ref/urlresolvers/#reverse-lazy
from django.urls import reverse_lazy


toggle = '-'


def base_function(request):
    if request.user.id is not None:
        user = request.user.get_username()
    else:
        user = None
    context = {"user": user}
    return context


def index(request):     # Home page
    context = base_function(request)
    return render(request, "coderdojomobile/index.html", context)


def scratch(request, liv):
    if liv == 'L*':
        elenco = Libro.objects.order_by('titolo').filter(
            genere__descrizione='scratch'
        )
        context = {
            'titolo_liv': "Scratch - Tutti livelli",
            'lista': elenco
        }
    else:
        elenco = Libro.objects.order_by('titolo').filter(
            livello=liv,
            genere__descrizione='scratch'
        )
        context = {
            'titolo_liv': "Scratch - Livello " + liv[-1:],
            'lista': elenco
        }
    return render(request, "coderdojomobile/libri.html", context)


def python(request, liv):
    if liv == 'L*':
        elenco = Libro.objects.order_by('titolo').filter(
            genere__descrizione='python'
        )
        context = {
            'titolo_liv': "Python - Tutti livelli",
            'lista': elenco
        }
    else:
        elenco = Libro.objects.order_by('titolo').filter(
            livello=liv,
            genere__descrizione='python'
        )
        context = {
            'titolo_liv': "Python - Livello " + liv[-1:],
            'lista': elenco
        }
    return render(request, "libri.html", context)


def html(request, liv):
    if liv == 'L*':
        elenco = Libro.objects.order_by('titolo').filter(
            genere__descrizione='html'
        )
        context = {
            'titolo_liv': "HTML - Tutti livelli",
            'lista': elenco
        }
    else:
        elenco = Libro.objects.order_by('titolo').filter(
            livello=liv,
            genere__descrizione='html'
        )
        context = {
            'titolo_liv': "HTML - Livello " + liv[-1:],
            'lista': elenco
        }
    return render(request, "libri.html", context)


def java(request, liv):
    if liv == 'L*':
        elenco = Libro.objects.order_by('titolo').filter(
            genere__descrizione='java'
        )
        context = {
            'titolo_liv': "Java - Tutti livelli",
            'lista': elenco
        }
    else:
        elenco = Libro.objects.order_by('titolo').filter(
            livello=liv,
            genere__descrizione='java'
        )
        context = {
            'titolo_liv': "Java - Livello " + liv[-1:],
            'lista': elenco
        }
    return render(request, "libri.html", context)


def php(request, liv):
    if liv == 'L*':
        elenco = Libro.objects.order_by('titolo').filter(
            genere__descrizione='php'
        )
        context = {
            'titolo_liv': "PHP - Tutti livelli",
            'lista': elenco
        }
    else:
        elenco = Libro.objects.order_by('titolo').filter(
            livello=liv,
            genere__descrizione='php'
        )
        context = {
            'titolo_liv': "PHP - Livello " + liv[-1:],
            'lista': elenco
        }
    return render(request, "libri.html", context)


def arduino(request, liv):
    if liv == 'L*':
        elenco = Libro.objects.order_by('titolo').filter(
            genere__descrizione='arduino'
        )
        context = {
            'titolo_liv': "Arduino - Tutti livelli",
            'lista': elenco
        }
    else:
        elenco = Libro.objects.order_by('titolo').filter(
            livello=liv,
            genere__descrizione='arduino'
        )
        context = {
            'titolo_liv': "Arduino - Livello " + liv[-1:],
            'lista': elenco
        }
    return render(request, "libri.html", context)


# Per compilare il DB
def genDB(request):
    with open(
        os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "toolbox/static/toolbox/elenco.txt"
        ),
        "r"
    ) as f:
        titoli = f.readlines()

    elenco = dict()
    cont = 0
    for t in titoli:
        if t[0:6] != 'elenco':
            elenco[cont] = t[:-5]
            unacard = (Libro.objects.order_by('titolo')
                       .filter(titolo=elenco[cont]))
            if len(unacard) == 0:  # il titolo non è ancora in DB
                # CheGenere = Genere(descrizione='scratch')
                # CheAutore = Autore(cognome='Coderdojo', nome='Generico')
                print(
                    Genere.objects.order_by('descrizione')
                    .filter(descrizione='scratch')[0],
                    Autore.objects.order_by('cognome')
                    .filter(cognome='Coderdojo')[0]
                )
                Card = Libro(
                    titolo=elenco[cont],
                    genere=Genere.objects.order_by('descrizione')
                    .filter(descrizione='scratch')[0],
                    autore=Autore.objects.order_by('cognome')
                    .filter(cognome='Coderdojo')[0]
                )
                Card.save()
                # print(Card)
            cont += 1
    # elenco=dict()
    # for libro in Libro.objects.all().order_by('titolo'):
    #    elenco[libro.titolo] = libro.posizione
    context = {'file_dict': elenco}
    return render(request, "genDB.html", context)


# Pagina con elenco delle liberatorie
def liberatorie(request, spec):
    global toggle
    toggle = ('' if toggle == '-' else '-')
    if spec == 'cogn':
        elenco = Liberatoria.objects.all().order_by(toggle+'cognome')
    elif spec == 'nome':
        elenco = Liberatoria.objects.all().order_by(toggle+'nome')
    elif spec == 'cons':
        elenco = Liberatoria.objects.all().order_by(toggle+'consegnata')
    else:
        elenco = Liberatoria.objects.all().order_by(toggle+'data_di_consegna')

    for libera in elenco:
        libera.consegnata = (
            unicodedata.lookup("HEAVY CHECK MARK") if libera.consegnata
            else " "
        )
    context = {'lista': elenco}
    return render(request, "liberatorieLista.html", context)


def nonraggiungibile(request):
    return HttpResponse(
        "<h2>Sito non raggiungibile. Accesso a internet inesistente"
    )


def split_software_by_os(op_sys_list, sw_list):
    # TODO hic sunt leones, test / refactor
    os_map = {}
    for op_sys in op_sys_list:
        os_map[op_sys.title] = []
    for sw in sw_list:
        for op_sys in os_map.keys():
            for supported_os in sw.operating_systems.all():
                if supported_os.title == op_sys:
                    os_map[op_sys].append(sw)
                    break
    return os_map


def softwareDojo(request, topic_id):
    context = base_function(request)
    # TODO filter by operating system
    op_sys = OperatingSystem.objects.all().order_by('title')
    tools = SoftwareTool.objects.filter(topic_id=topic_id).order_by('title')
    sw_map = split_software_by_os(op_sys, tools)
    context.update({
        'sw_by_os': sw_map})
    return render(request, "coderdojomobile/softwareDojo.html", context)


# Usiamo le categorie definite a db
def sprites(request):
    context = base_function(request)
    sprite_categories = SpriteCategory.objects.order_by('sprite_category_name')
    context.update({
        'sprite_categories': sprite_categories
    })
    return render(request, 'coderdojomobile/sprites.html', context)


def spritesAlieni(request):
    context = base_function(request)
    return render(request, "spritesAlieni.html", context)


def spriteCategory(request, category_id):
    context = base_function(request)
    sprites = Sprite.objects.order_by('sprite_name').filter(
        spritecategory__id=category_id
    )
    sprite_images = SpriteImages.objects.all().filter(
        sprite__in=sprites
    ).order_by('image_order')
    for sprite in sprites:
        sprite.imgs = []
        for image in sprite_images:
            if image.sprite.id == sprite.id:
                sprite.imgs.append(image)
    context.update({
        'sprites': sprites,
        'sprite_images': sprite_images
    })
    return render(request, 'coderdojomobile/spritesInCategory.html', context)


def learningTopicGuides(request):
    context = base_function(request)
    learning_topics = LearningTopic.objects.order_by('title')
    context.update({
        'learning_topics': learning_topics
    })
    return render(
                 request,
                 'coderdojomobile/learningTopicsGuides.html',
                 context
                 )


def learningTopicSoftwares(request):
    context = base_function(request)
    learning_topics = LearningTopic.objects.order_by('title')
    context.update({
        'learning_topics': learning_topics
    })
    return render(
                 request,
                 'coderdojomobile/learningTopicsSoftware.html',
                 context
                 )


def events(request):
    context = base_function(request)
    sorted_events = Event.objects.order_by('event_date')
    context.update({
        'events': sorted_events,
    })
    return render(request, 'coderdojomobile/events.html', context)


def add_waiver_status_to_ticket(ticket):
    ticket.has_valid_waiver = has_valid_waiver(ticket)


def eventDetails(request, event_id):
    context = base_function(request)
    event = Event.objects.order_by('event_date').get(id=event_id)
    tickets = Ticket.objects.order_by('participant__name').filter(
        event__id=event_id
    )
    total_participants = tickets.count()
    missing_participants = 0
    for ticket in tickets:
        if not ticket.has_checked_in:
            missing_participants = missing_participants + 1
    total_participants = tickets.count()
    # Navigate participants from tickets of this event
    queryset_for_form = Participant.objects.filter(ticket__event__id=event_id)
    participants = queryset_for_form
    for ticket in tickets:
        for participant in participants:
            if participant.id == ticket.participant.id:
                add_waiver_status_to_ticket(ticket)
                ticket.badges = []
                for part_badge in participant.badges.all():
                    ticket.badges.append(part_badge)
    form = CheckInOutForm(queryset_for_form)
    context.update({
        'event': event,
        'tickets': tickets,
        'form': form,
        'total_participants': total_participants,
        'missing_participants': missing_participants
    })
    return render(request, 'coderdojomobile/eventDetails.html', context)


def is_valid_waiver_for_event(waiver, event):
    return waiver is not None \
           and waiver.valid \
           and (waiver.expiry_date is None
                or waiver.expiry_date > event.event_date)


def has_valid_waiver(ticket):
    waiver = None
    waiver_valid = False
    try:
        waiver = ticket.participant.waiver
    except ObjectDoesNotExist:
        waiver = None
    waiver_valid = is_valid_waiver_for_event(waiver, ticket.event)
    return waiver_valid


@permission_required(
    'coderdojomobile.change_ticket',
    login_url=reverse_lazy('coderdojomobile:login',
                           current_app="coderdojomobile")
)
def eventCheckInOut(request, event_id):
    context = base_function(request)
    if request.method == 'POST':  # fix get
        # create a form instance and populate it with data from the request:
        # Navigate participants from tickets of this event
        queryset = Participant.objects.filter(ticket__event__id=event_id)
        form = CheckInOutForm(queryset_for_form=queryset, data=request.POST)
        ticket = None
        event = None
        ticket_found = False
        waiver_valid = False
        try:
            event = Event.objects.get(id=event_id)
        except ObjectDoesNotExist:
            event = None
        if form.is_valid():
            # Check which field is populated
            try:
                if (len(form.cleaned_data['participant_id']) > 0):
                    ticket = Ticket.objects.get(
                        event__id=event_id,
                        participant__uuid=form.cleaned_data['participant_id']
                    )
                elif (len(form.cleaned_data['ticket_id']) > 0):
                    ticket = Ticket.objects.get(
                        event__id=event_id,
                        uuid=form.cleaned_data['ticket_id']
                    )
                elif not (form.cleaned_data['participant'] is None):
                    ticket = Ticket.objects.get(
                        event__id=event_id,
                        participant__id=form.cleaned_data['participant'].id
                    )
            except ObjectDoesNotExist:
                ticket = None
            if not (ticket is None):  # We found the ticket, set status
                ticket_found = True
                if form.cleaned_data['check_in_out'] == form.CHECK_IN:
                    ticket.has_checked_in = True
                else:
                    ticket.has_checked_in = False
                ticket.save()
                # check waiver status
                waiver_valid = has_valid_waiver(ticket)
        context.update({
            'ticket': ticket,
            'event': event,
            'waiver_is_valid': waiver_valid,
            'ticket_found': ticket_found
        })
        return render(request, 'coderdojomobile/eventCheckInOut.html', context)


# -----------------------------------------------------------------------------
# Function usate per prova
def libro(request, id):
    try:
        libro = Libro.objects.get(pk=id)
        return HttpResponse(
            "'%s' di %s, %s<br>" % (libro.titolo, libro.autore, libro.genere)
        )
    except Libro.DoesNotExist:
        return HttpResponse("Codice %s inesistente" % id)


def lista(request):
    elenco = dict()
    for libro in Libro.objects.all().order_by('titolo'):
        elenco[libro.titolo] = libro.posizione
    context = {'file_dict': elenco}
    return render(request, "libriLista.html", context)
