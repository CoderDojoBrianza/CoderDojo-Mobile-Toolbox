# Installing

This is a summary of installation steps, with references to other tutorials / guides for single steps

## Dependencies

- Python3
- Django
- A web server (e.g. Apache)
- Jquery 3.3.1
- Bootstrap3
- HTML5 shiv
- Respond.js

## Steps

Setting up CoderDojo mobile requires two major steps:

- Setting up the base system [#setting up the base system]
- Setting up the app [#setting up the app]
- Customized the app [#customize the app]

To install CoderDojo mobile you must follow these steps:

### Setting up the base system 

Prepare the base system (see the [References](#references) section) :
- install Python 3
- install Django 
- installing a web server

Optionally, if you want a fully autonomous Raspberry PI box (wireless access point, DNS, etc) you need to [configure hostapd and dnsmasq](https://www.raspberrypi.org/documentation/configuration/wireless/access-point.md)

### Setting up the app

Steps:

- [Create a Django project](https://docs.djangoproject.com/en/2.0/intro/tutorial01/#creating-a-project) 
- Configure `settings.py`
- Create a `toolbox/libraries` folder inside the `coderdojomobile` folder
- Download dependencies:
	- [JQuery](https://jquery.com/) put the `jquery-3.3.1.min.js` file in the `toolbox/libraries` folder
	- [Bootstrap3](https://getbootstrap.com/docs/3.3/). Put the entire bootstrap folder in the `toolbox/libraries` folder
	- [HTML5shiv](https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js) : put the  `html5shiv.min.js` file in the `toolbox/libraries` folder
	- [RespondJs](https://oss.maxcdn.com/respond/1.4.2/respond.min.js) : put the `respond.min.js` file in the `toolbox/libraries` folder

The `toolbox/libraries` folder should look like this:

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

**TODO steps**: creating a Django folder, installing and configuring the app

### Customize the app

You can customize logos and images to match those of your Dojo.

All customizable files are in the `\toolbox\custom-brand` folder:

- The `favicon` file 
- The home logo file 

## References

All the first steps can be performed following these guides:

- [Installing Apache on Raspberry](https://www.raspberrypi.org/documentation/remote-access/web-server/apache.md)
- [Installing Django on Apache - Mod WSGI](https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-debian-8)

