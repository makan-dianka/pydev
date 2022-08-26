from django.shortcuts import render 
import logging

log = logging.getLogger('log')


def index(request):
    log.error("Message for error")
    return render(request, 'myapp/index.html')