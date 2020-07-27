from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from urllib.parse import urlencode
from django.template import loader
from django.http import FileResponse, Http404
# Custom imports added
# Need timezone for date/time published
from django.utils import timezone
import datetime
# These are needed for user authentication and persistence
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    template = loader.get_template('main/index.html')
    context = {     #all inputs for the html go in these brackets
        
    }
    return HttpResponse(template.render(context, request))
