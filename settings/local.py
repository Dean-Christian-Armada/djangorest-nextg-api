from .base import *
import socket

DATABASES['default']['TEST'] = { 'NAME' : socket.gethostname() + DATABASES['default']['NAME']}
