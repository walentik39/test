#!/usr/bin/env python3

import sys
from socket import *
serverHost = 'localhost' # имя сервера, например: 'starship.python.net'
serverPort = 50007
message = [b'Hello network world']
if len(sys.argv) > 1:
    serverHost = sys.argv[1]
    if len(sys.argv) > 2:
        message = (x.encode() for x in sys.argv[2:])
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, serverPort))

for line in message:
    sockobj.send(line)
    data = sockobj.recv(1024)
    print('Client receved:', data)
sockobj.close()
