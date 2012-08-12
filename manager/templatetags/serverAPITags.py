import sys
import signal
import time
import socket

from django import template
from manager import serverAPI
from manager.serverAPI import MinecraftQuery

register = template.Library()

class TimeoutException(Exception):
    pass

def status(name):
    """Returns the status of a server from the given servername"""
    statuses = { -1: "Error",
		  0: "Stopped",
		  1: "Running",
	       }
    #return "status(" + value + "): " + str(serverAPI.status(value))
    return statuses[serverAPI.status(name)]

def players(port):
    """Returns the number of players on a server"""
    try:
	return MinecraftQuery("localhost",port,timeout=0.1).get_status()['numplayers']
    except socket.timeout:
	return "timeout"

register.filter('status', status)
register.filter('players', players)
