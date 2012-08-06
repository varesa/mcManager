from django.core.urlresolvers   import reverse
from django.http                import HttpResponseRedirect
from django.template            import RequestContext
from django.shortcuts           import get_list_or_404, get_object_or_404, render_to_response, redirect
from django.contrib.auth        import authenticate, login, logout
from django.contrib.auth.models import User

from manager.models import Server

def admin_index(request):
    """Allows the user to choose between administration tasks"""
    if request.user.is_authenticated():
        if request.user.has_perm('manager.index_view'):
            servers = list(Server.objects.all())
            return render_to_response('admin_index.html', {}, context_instance=RequestContext(request))
        else:
            error = 'You do not have the required permissions to view this page.'
            return render_to_response('error.html', {'errormsg':error}, context_instance=RequestContext(request))
        
    else:
        return redirect('servermanager.views.login_', location='servers.views.admin_index') # Ask user to log in, provide a location to go to after logging in
        
def admin_servers(request):
    """Allows user to manage game-servers"""
    if request.user.is_authenticated():
        if request.user.has_perm('admin_servers'):
            servers = list(Server.objects.all())
            return render_to_response('admin_servers.html', {'servers':servers}, context_instance=RequestContext(request))
        else:
            error = 'You do not have the required permissions to view this page.'
            return render_to_response('error.html', {'errormsg':error}, context_instance=RequestContext(request))
        
    else:
        return redirect('servermanager.views.login_', location='servers.views.admin_servers') # Ask user to log in, provide a location to go to after logging in

def admin_users(request):
    users = User.objects.all().order_by('username')
    
def admin_permissions(request):
    pass
    
def admin_settings(request):
    """abc"""
    pass