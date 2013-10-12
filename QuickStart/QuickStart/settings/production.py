# Production configuration
from django.conf import settings
import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['YOUR_DOMAIN.com', 'www.YOUR_DOMAIN.com']

# Backend storage configuration
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = DEFAULT_FILE_STORAGE

# SendGrid email settings
EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# AWS settings to serve static files from S3
AWS_ACCESS_KEY_ID = os.environ['AWS_KEY']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']

# URL for static content
STATIC_URL = '//s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
