==========
Installing
==========

This is a summary of installation steps, with references to other
tutorials / guides for single steps

Dependencies
------------

-  Python3
-  Django
-  Jquery 3.3.1
-  Bootstrap3
-  HTML5 shiv
-  Respond.js

For production use we strongly reccommend using a web server
(e.g. Apache)

Steps
-----

Setting up CoderDojo mobile requires four major steps:

-  `Setting up the base system`_
-  `Setting up the app`_
-  `Creating content`_
-  `Customizing the app`_

Setting up the base system
~~~~~~~~~~~~~~~~~~~~~~~~~~

Prepare the base system (see the `References`_ section) : 

-  install Python 3 
-  install Django 
-  install `django-bootstrap-3`_ 
-  install a web server

Optionally, if you want a fully autonomous Raspberry PI box (wireless
access point, DNS, etc) you need to `configure hostapd and dnsmasq`_

Setting up the app
~~~~~~~~~~~~~~~~~~

Steps:

1. `Create a Django project`_, with any name you want. If you want to
   follow the instructions more easily, call it ``toolbox``.
2. Download / Clone the Git repository to a ``coderdojomobile`` folder
   inside the project one. Supposing your project name is ``toolbox``,
   the structure should look like this:

   ::

          toolbox
          │
          └─── coderdojomobile <- clone it here
          │    └─── .git
          │    └─── doc
          │    └─── migrations
          │    └─── ... etc etc ...
          └─── toolbox
          └─── db.sqlite3
          └─── manage.py

3. Configure ``settings.py`` in the ``toolbox`` folder:

   1. add the app, and the ``bootstrap3`` app, to the installed apps:

      ::

             INSTALLED_APPS = [
                 'django.contrib.admin',
                 'django.contrib.auth',
                 'django.contrib.contenttypes',
                 'django.contrib.sessions',
                 'django.contrib.messages',
                 'django.contrib.staticfiles',
                 'django.contrib.admindocs',
                 'coderdojomobile.apps.CoderDojoMobileAppConfig', #configure the app
                 'bootstrap3' # 
             ]

   2. set the allowed urls:

      ::

             ALLOWED_HOSTS = ["localhost","coderdojomobile","127.0.0.1"]

   3. configure static file settings. See also `Installing Django on
      Apache - Mod WSGI`_ for explanation on the static files
      configuration

      ::

          # Static files (CSS, JavaScript, Images)
          # https://docs.djangoproject.com/en/2.0/howto/static-files/

          STATIC_URL = '/static/'

          STATICFILES_DIRS = [
              os.path.join(BASE_DIR, "coderdojomobile/static"),
          ]

          STATIC_ROOT="/home/pi/Documents/CDLSMBTK3/MYSTATIC" #Customize this with your static folder on the filesystem

   4. set MEDIA_URL and MEDIA_ROOT (example, set to the correct media
      folder):

      ::

         MEDIA_URL = '/media/'
         MEDIA_ROOT = '/home/pi/media' #example

   5. activate localization:

      ::

         MIDDLEWARE = [
         'django.middleware.security.SecurityMiddleware',
         'django.contrib.sessions.middleware.SessionMiddleware',
         'django.middleware.common.CommonMiddleware',
         'django.middleware.csrf.CsrfViewMiddleware',
         'django.contrib.auth.middleware.AuthenticationMiddleware',
         'django.contrib.messages.middleware.MessageMiddleware',
         'django.middleware.clickjacking.XFrameOptionsMiddleware',
         'django.middleware.locale.LocaleMiddleware' #localization
         ]

   6. configure locale path:

      ::

         LOCALE_PATHS = [
             '/home/pi/toolbox/coderdojomobile/locale', #examples, set your own
         ]

4. Add the application to the ``urlpatterns`` in the ``toolbox/urls.py``
   file:

   ::

      urlpatterns = [
          path('coderdojomobile/', include('coderdojomobile.urls')),
          path('admin/doc', include('django.contrib.admindocs.urls')),
          path('admin/', admin.site.urls),
      ] 

5. to make media files work also in ``DEBUG`` mode, during development,
   add these lines to the ``toolbox/urls.py`` file:

   1. Beginning of the file:

      ::

             from . import settings
             from django.conf.urls.static import static

   2. at the end:

      ::

             if settings.DEBUG:
                 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

6. Create a ``toolbox/libraries`` folder inside the ``coderdojomobile``
   folder
7. Download dependencies:

   1. `JQuery`_ put the ``jquery-3.3.1.min.js`` file in the
      ``toolbox/libraries`` folder
   2. `Bootstrap3`_. Put the entire bootstrap folder in the
      ``toolbox/libraries`` folder
   3. `HTML5shiv`_ : put the ``html5shiv.min.js`` file in the
      ``toolbox/libraries`` folder
   4. `RespondJs`_ : put the ``respond.min.js`` file in the
      ``toolbox/libraries`` folder

8. Check folder structure: The ``coderdojomobile/toolbox/libraries``
   folder should look like this:

   ::

              coderdojomobile/toolbox/libraries
              │
              └─── bootstrap-3
              │   └─── css
              │   └─── font
              │   └─── js
              └─── html5shiv.min.js
              └─── jquery-3.3.1.min.js
              └─── jumbotron.css
              └─── respond.min.js

9. Initialize the DB with the ``./manage.py migrate`` command

10. Compile local translations:

   ::

      django-admin compilemessages

Running the app
~~~~~~~~~~~~~~~

You can run the app using the embedded webserver provided by Django:

::

   python manage.py runserver

In production, you’ll have to start Apache. Refer to your system’s
guides for this step. When using an external web server, remember to
collect static files:

::

   python manage.py collectstatic 

Also, remember to configure the media folder in the
``/etc/apache2/sites-available/000-default.conf`` file (example):

::


       Alias /media /home/pi/media
       <Directory /home/pi/media>
           Require all granted
       </Directory>

Creating content
~~~~~~~~~~~~~~~~

Of course, when you first run the app, it will be empty. To actually use
it, you need to provide some content. Currently the app offers only very
limited content upload capabilities, so you’ll have to initialize
database tables using the admin interface / a tool to modify database
tables, like `DB Browser for sqlite`_

Customizing the app
~~~~~~~~~~~~~~~~~~~

You can customize logos and images to match those of your Dojo.

All customizable files are in the ``static\toolbox\custom-brand``
folder:

-  The ``favicon`` file

References
----------

All the first steps can be performed following these guides:

-  `Installing Apache on Raspberry`_
-  `Installing Django on Apache - Mod WSGI`_

.. _DB Browser for sqlite: https://sqlitebrowser.org/
.. _Installing Apache on Raspberry: https://www.raspberrypi.org/documentation/remote-access/web-server/apache.md
.. _Setting up the base system: #setting-up-the-base-system
.. _Setting up the app: #setting-up-the-app
.. _Creating content: #creating-content
.. _Customizing the app: #customize-the-app
.. _References: #references
.. _django-bootstrap-3: https://github.com/dyve/django-bootstrap3
.. _configure hostapd and dnsmasq: https://www.raspberrypi.org/documentation/configuration/wireless/access-point.md
.. _Create a Django project: https://docs.djangoproject.com/en/2.0/intro/tutorial01/#creating-a-project
.. _Installing Django on Apache - Mod WSGI: https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-debian-8
.. _JQuery: https://jquery.com/
.. _Bootstrap3: https://getbootstrap.com/docs/3.3/
.. _HTML5shiv: https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js
.. _RespondJs: https://oss.maxcdn.com/respond/1.4.2/respond.min.js