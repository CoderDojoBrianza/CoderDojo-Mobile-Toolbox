from django.urls import path, reverse_lazy
from . import views
from . import views_tutorial
from django.contrib.auth import views as auth_views

app_name = 'coderdojomobile'
urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('scratch/<str:liv>/', views.scratch, name='scratch'),
    path('python/<str:liv>/', views.python, name='python'),
    path('html/<str:liv>/', views.html, name='html'),
    path('java/<str:liv>/', views.java, name='java'),
    path('php/<str:liv>/', views.php, name='php'),
    path('arduino/<str:liv>/', views.arduino, name='arduino'),
    path('genDB/', views.genDB, name='genDB'),
    path(
        'liberatorie/<str:spec>/',
        views.liberatorie,
        name='liberatorie-cogn'
        ),
    path('nonraggiungibile/', views.nonraggiungibile, name='nonraggiungibile'),
    path(
        'learningTopicSoftwares/',
        views.learningTopicSoftwares,
        name='softwareTopics'
    ),
    path('soft/<int:topic_id>', views.softwareDojo, name='soft'),
    path('sprites/', views.sprites, name='sprites'),
    path('spritesAlieni/', views.spritesAlieni, name='spritesAlieni'),
    path(
        'tutorial/<int:tutorial_id>',
        views_tutorial.tutorial,
        name='tutorial'
        ),
    path(
        'spriteCategory/<int:category_id>/',
        views.spriteCategory,
        name='spriteCategory'
    ),
    path('thanks_tutorial/', views_tutorial.thanks, name='thanks'),
    path('thanks_rating/', views_tutorial.thanks_rating, name='rating_thanks'),
    path('rating_error/', views_tutorial.rating_error, name='rating_error'),
    path(
        'learningTopicGuides/',
        views.learningTopicGuides,
        name='learningTopicGuides'
        ),
    path(
        'learningTopics/<int:topic_id>/',
        views_tutorial.tutorials,
        name='tutorials'
        ),
    path('events/', views.events, name='events'),
    path(
        'eventDetails/<int:event_id>',
        views.eventDetails,
        name='eventDetails'
        ),
    path(
        'eventDetails/check_in_out/<int:event_id>',
        views.eventCheckInOut,
        name='eventCheckInOut'
        ),
    path(
        'eventDetails/ticket_upload/<int:event_id>',
        views.event_ticket_upload,
        name='event_ticket_upload'
        ),
    path(
        'login/',
        auth_views.LoginView.as_view(
                                    template_name='coderdojomobile/login.html'
                                    ),
        name="login"),
    path(
        'logout/',
        auth_views.LogoutView
        .as_view(next_page=reverse_lazy('coderdojomobile:index')),
        name="logout"
        ),
    # views non funzionali per il progetto ma solo per prova
    path('lista/', views.lista, name='lista'),
    path('libro/<int:id>/', views.libro, name='libro'),
]
