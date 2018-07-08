# Installing

This is a summary of installation steps, with references to other tutorials / guides for single steps

## Dependencies

- Python3
- Django
- Jquery 3.3.1
- Bootstrap3
- HTML5 shiv
- Respond.js

For production use we strongly reccommend using a web server (e.g. Apache)

## Steps

Setting up CoderDojo mobile requires three major steps:

- [Setting up the base system](#setting-up-the-base-system)
- [Setting up the app](#setting-up-the-app)
- [Customized the app](#customize-the-app)


### Setting up the base system 

Prepare the base system (see the [References](#references) section) :
- install Python 3
- install Django 
- installing a web server

Optionally, if you want a fully autonomous Raspberry PI box (wireless access point, DNS, etc) you need to [configure hostapd and dnsmasq](https://www.raspberrypi.org/documentation/configuration/wireless/access-point.md)

### Setting up the app

Steps:

1. [Create a Django project](https://docs.djangoproject.com/en/2.0/intro/tutorial01/#creating-a-project) 
1. Configure `settings.py`:
    1. add the app to the installed apps:

        ```
            INSTALLED_APPS = [
                'django.contrib.admin',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.staticfiles',
                'django.contrib.admindocs',
                'coderdojomobile.apps.CoderDojoMobileAppConfig', #configure the app
            ]
        ```

    1. set the allowed urls:

        ```
            ALLOWED_HOSTS = ["localhost","coderdojomobile","127.0.0.1"]
        ```

    1. configure static file settings. See also [Installing Django on Apache - Mod WSGI](https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-debian-8) for explanation on the static files configuration

        ```

            # Static files (CSS, JavaScript, Images)
            # https://docs.djangoproject.com/en/2.0/howto/static-files/

            STATIC_URL = '/static/'

            STATICFILES_DIRS = [
                os.path.join(BASE_DIR, "coderdojomobile/static"),
            ]

            STATIC_ROOT="/home/pi/Documents/CDLSMBTK3/MYSTATIC" #Customize this with your static folder on the filesystem
        ```

    1. set MEDIA_URL and MEDIA_ROOT in your project’s `settings.py` (example, set to the correct media folder):

        ```
        MEDIA_URL = '/media/'
        MEDIA_ROOT = '/var/www/example.com/media/'
        ```

1. to make media files work also in `DEBUG` mode, during development, add these lines to the `urls.py` of your **project** (not to the app's one):
    1. Beginning of the file:

        ```
            from . import settings
            from django.conf.urls.static import static
        ```

    1. at the end:

        ```
            if settings.DEBUG:
                urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        ```

1. Create a `toolbox/libraries` folder inside the `coderdojomobile` folder
1. Download dependencies:
	1. [JQuery](https://jquery.com/) put the `jquery-3.3.1.min.js` file in the `toolbox/libraries` folder
	1. [Bootstrap3](https://getbootstrap.com/docs/3.3/). Put the entire bootstrap folder in the `toolbox/libraries` folder
	1. [HTML5shiv](https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js) : put the  `html5shiv.min.js` file in the `toolbox/libraries` folder
	1. [RespondJs](https://oss.maxcdn.com/respond/1.4.2/respond.min.js) : put the `respond.min.js` file in the `toolbox/libraries` folder

1. Check folder structure: The `toolbox/libraries` folder should look like this:

    ```
        toolbox/libraries
        │
        └───bootstrap-3
        │   └───css
        │   └───font
        │   └───js
        │   html5shiv.min.js
        │   jquery-3.3.1.min.js
        │   jumbotron.css
        │   respond.min.js
    ```

1. Initialize the DB with the `./manage.py migrate` command
1. Collect static files with the `./manage.py collectstatic` command

### Customize the app

You can customize logos and images to match those of your Dojo.

All customizable files are in the `\toolbox\custom-brand` folder:

- The `favicon` file 

## References

All the first steps can be performed following these guides:

- [Installing Apache on Raspberry](https://www.raspberrypi.org/documentation/remote-access/web-server/apache.md)
- [Installing Django on Apache - Mod WSGI](https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-debian-8)

