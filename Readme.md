Django-Quickstart
===

Base Django application with some helpful modifications for deploying in to Heroku using different configurations.

Remember to:

* Update the SECRET_KEY in QuickStart/settings/common.py
* Update the ALLOWED_HOSTS in QuickStart/settings/production.py

If you change the application name, you need to update all references to 'QuickStart' in the locations:
* QuickStart.settings.common in wsgi.py
* ROOT_URLCONF, WSGI_APPLICATION, LOGGING in QuickStart/settings/common.py


