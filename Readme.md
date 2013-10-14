Django-Quickstart
===

Base Django application with some helpful modifications for deploying in to Heroku using different configurations.

How to use
---

Clone the repo:

```
git clone https://github.com/mgoldsborough/django-quickstart/ YourAwesomeApp
```

Create virtual environment:
```
cd YourAwesomeApp
virtualenv venv
```

Activate!

```
source venv/bin/activate
```

Install dependencies via pip:
```
pip installl -r requirements.txt
```

Update application settings:

* Update the SECRET_KEY in QuickStart/settings/common.py
* Update the ALLOWED_HOSTS in QuickStart/settings/production.py

Update references to QuickStart:


* QuickStart and QuickStart/QuickStart folders
* Procfile

```
web: python YourAwesomeApp/manage.py runserver 0:$PORT
```

* QuickStart.settings.common in wsgi.py

```
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "YourAwesomeApp.settings.common")
```
* ROOT_URLCONF, WSGI_APPLICATION, LOGGING in QuickStart/settings/common.py

Fire that puppy up:
```
python YourAwesomeApp/manage.py runserver
```

Go to localhost:8000. ???. Profit!

Dependencies
---
[python](http://www.python.org/)
[virtualenv](https://pypi.python.org/pypi/virtualenv)

pip takes care of the rest.
