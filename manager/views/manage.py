from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import get_list_or_404, get_object_or_404, render_to_response, redirect
from django.contrib.auth import authenticate, login, logout

from manager.models import Server

def manage_index(request, serverid=False):
    """Shows the status of servers"""
    if request.user.is_authenticated():
        if serverid:
            server = Server.objects.get(pk=serverid)
        else:
            server = False
        return render_to_response('manage_index.html', {'server': server, 'servers':Server.objects.all(), 'username': request.user.username}, context_instance=RequestContext(request))
        
    else:
        return redirect('servermanager.views.login_', location='servers.views.manage') # Ask user to log in, provide a location to go to after logging in