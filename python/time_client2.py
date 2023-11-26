#!/usr/bin/env python3

import socket
def fun():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        host = "time.nist.gov"
        port = 13

        s.connect((host, port))
        s.sendall(b'')
        return (str(s.recv(4096), 'utf-8'))

def file_write(name):
    with open('test5.odt','w') as file:
        file.write(name)


def file_read(name):
    with open('test5.odt','r') as f:
        for i in f:
            print(i, end='')

if __name__=='__main__':
    res = file_write(fun())
    res2 = file_read(res)
