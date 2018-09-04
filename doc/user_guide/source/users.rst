============
Users
============

Currently, the two main features are learning material/tools, and events. Their configuration is mainly performed using the Django Admin site.

So, you need to create at least one admin user, as shown in the `django user guide`_.

.. _django user guide: https://docs.djangoproject.com/en/2.1/intro/tutorial02/#creating-an-admin-user


Generally, the toolbox will be used by Ninjas and Mentors. You don't need to create Django users for Ninjas. For Mentors, you'll need to create django users with change permissions to ``coderdojomobile|learning material`` and ``coderdojomobile|ticket``.

