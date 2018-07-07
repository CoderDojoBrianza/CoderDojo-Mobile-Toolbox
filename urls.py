from django.urls import path
from . import views
from . import views_tutorial

app_name = 'coderdojomobile'
urlpatterns = [
	path('', views.index, name='index'),
	path('scratch/<str:liv>/', views.scratch, name='scratch'),
	path('python/<str:liv>/', views.python, name='python'),
	path('html/<str:liv>/', views.html, name='html'),
	path('java/<str:liv>/', views.java, name='java'),
	path('php/<str:liv>/', views.php, name='php'),
	path('arduino/<str:liv>/', views.arduino, name='arduino'),
	path('genDB/', views.genDB, name='genDB'),
	path('liberatorie/<str:spec>/', views.liberatorie, name='liberatorie-cogn'),
	path('nonraggiungibile/', views.nonraggiungibile, name='nonraggiungibile'),
	path('soft/', views.softwareDojo, name='soft'),
	path('sprites/', views.sprites, name='sprites'),
	path('spritesAlieni/', views.spritesAlieni, name='spritesAlieni'),
	path('tutorials/', views_tutorial.tutorials, name='tutorials'),
	path('tutorial/<int:tutorial_id>', views_tutorial.tutorial, name='tutorial'),
	path('spriteCategory/<int:category_id>/', views.spriteCategory, name='spriteCategory'),
    path('thanks_tutorial/', views_tutorial.thanks, name='thanks'),
    
# views non funzionali per il progetto ma solo per prova
    path('lista/', views.lista, name='lista'),
    path('libro/<int:id>/', views.libro, name='libro'),
]
#    path('scratch1/', views.scratch1, name='scratch1'),
