from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import get_list_or_404, get_object_or_404, render_to_response, redirect
from django.contrib.auth import authenticate, login, logout

from manager.models import Server

def status_index(request):
    """Shows the status of servers"""
    if request.user.is_authenticated():
        servers = list(Server.objects.all())
        
        
        return render_to_response('status_index.html', {'servers': servers}, context_instance=RequestContext(request))
    else:
        return redirect('manager.views.login_', location='manager.views.status_index') # Ask user to log in, provide a location to go to after logging in