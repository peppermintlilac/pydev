#!/usr/bin/python

import socket
import sys

if ( len(sys.argv) != 2 ):
    print "Usage: " + sys.argv[0] + " you must enter IP or FQDN"
    sys.exit(1)

remote_host = sys.argv[1]

for remote_port in [389,636]:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        try:
                sock.connect((remote_host, remote_port))
        except Exception,e:
                print "%d closed " % remote_port
        else:
                print "%d open" % remote_port
        sock.close()
