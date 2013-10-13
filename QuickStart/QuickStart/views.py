from django.shortcuts import render
from django.views.decorators.gzip import gzip_page
from django.views.decorators.http import require_GET
import logging


logger = logging.getLogger(__name__)

@gzip_page
@require_GET
def home(request):
    return render(request, 'home.html')