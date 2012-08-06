from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import get_list_or_404, get_object_or_404, render_to_response, redirect
from django.contrib.auth import authenticate, login, logout

import status # "views.status(.py)"

def index(request):
    """Homepage for server-management"""
    return status.status_index(request)