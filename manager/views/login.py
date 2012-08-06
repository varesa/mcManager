from django.shortcuts import get_list_or_404, get_object_or_404, render_to_response, redirect
from django.template import RequestContext

from django.contrib.auth import authenticate, login, logout


def login_(request,location='manager.views.index'):
    """Provide a login-screen to the user"""
    try:
	return render_to_response('login.html', {'location':location, 'errormsg':request.session['loginerror']},context_instance=RequestContext(request))
    except KeyError:
	return render_to_response('login.html', {'location':location}, context_instance=RequestContext(request))
    

def login_action(request):
    """Log the user in"""
    username = request.POST['username']
    password = request.POST['password']
    location = request.POST['location']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect(location)
        else:
            pass
    else:
	request.session['loginerror'] = "Invalid username or password"
        return login_(request,location)
    
def logout_action(request):
    """Log the user out"""
    logout(request)
    return redirect('manager.views.status_index')