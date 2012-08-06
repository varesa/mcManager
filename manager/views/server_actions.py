from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from manager.models import Server

from manager import serverAPI


def start_server(request, serverid):
    """Starts a server"""
    if request.user.is_authenticated():
        try:
	    server = Server.objects.get(pk=serverid)
	#    if server.state == 'S':
	    serverAPI.start(server.name, server.path, server.command)
	    return HttpResponse('ok')
	#    else:
	#	return HttpResponse('not stopped')
	except ObjectDoesNotExist:
	    return HttpResponse('Server does not exist')
	
    else:
        return HttpResponse('permission denied')

def stop_server(request, serverid):
    """Stops a server"""
    if request.user.is_authenticated():
        try:
    	    server = Server.objects.get(pk=serverid)
#    	    if server.state == 'R':
	    serverAPI.stop(server.name)
	    return HttpResponse('ok')
#	    else:
#		return HttpResponse('not running')
	except ObjectDoesNotExist:
	    return HttpResponse('server does not exist')
    else:
        return HttpResponse('permission denied')