#!/usr/bin/env python
"""\
base_server.py : standalone communications server for Snap! sketches

This is written using only standard Python modules.  It operates as a standalone
HTTP server using the BaseHTTPServer class.

Copyright (c) 2016, Garth Zeglin. All rights reserved. Licensed under the
terms of the BSD 3-clause license as included in LICENSE.
"""

import argparse
import socket
import urlparse
import time
import BaseHTTPServer

import blackboard

################################################################
# single global storage object
bb = blackboard.BlackBoard()
        
################################################################
# The HTTPServer class is responsible for creating instances of this handler
# class.  In principle, a different instance of this class could be created for
# each connection.

class BlackBoardHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    def log_message(self, format, *args):
        # suppress the usual normal request log messages
        pass
    
    def do_HEAD(self):
        print "Received HEAD request."
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=UTF-8")
        self.send_header("Access-Control-Allow-Origin", "http://snap.berkeley.edu")
        self.end_headers()
        return
    
    def do_GET(self):
        """Respond to a GET request."""

        # Extract the namespace and query elements from the URL.
        # E.g. 'http:/server.net:7000/namespace?key1=value1&key2=value2&key3='
        # Parses 'namespace' as the namespace string and a key-value dictionary in query.

        global bb
        parsed    = urlparse.urlparse(self.path)
        namespace = bb.normalize_key(parsed.path.lstrip('/'))
        query     = urlparse.parse_qs(parsed.query, keep_blank_values=True)

        # Each query value from parse_qs is a list in case the same key appears
        # multiple times.  This reduces the query data to a plain dictionary
        # with string values; only the first value for each key is used.
        for key in query.keys():
            query[key] = query[key][0]

        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=UTF-8")
        # The following header field will specifically allow Javascript loaded from
        # the Snap! site to access this resource. For details, see: http://enable-cors.org/server.html
        self.send_header("Access-Control-Allow-Origin", "http://snap.berkeley.edu")
        self.end_headers()

        if namespace == "":
            self.wfile.write(bb.status_message())

        else:
            bb.update(namespace, query)
            # note: the BaseHTTPServer library assumes the data is a string, not unicode
            self.wfile.write(bb.data_message(namespace).encode('utf-8'))
            self.wfile.write("namespace " + namespace.encode('utf-8') + "\n")

        self.wfile.write("IP %s\n" % self.client_address[0])
        return
    
################################################################        
if __name__ == '__main__':

    # process command line arguments
    parser = argparse.ArgumentParser( description = """Server to process interprocess messaging requests over HTTP.""")
    parser.add_argument( '--verbose', action='store_true', help='Enable more detailed output.' )
    parser.add_argument( '--host', help='Specify the host name.')
    parser.add_argument( '--port', type=int, default=7000,help='Specify the TCP port number on which to serve HTTP requests.')
    args = parser.parse_args()

    host_name  = args.host if args.host is not None else socket.getfqdn()
    port_number = args.port
    
    httpd = BaseHTTPServer.HTTPServer((host_name, port_number), BlackBoardHandler)

    if args.verbose:
        print time.asctime(), "Server start: %s:%s" % (host_name, port_number)

    try:
        httpd.serve_forever()

    except KeyboardInterrupt:
        pass

    httpd.server_close()

    if args.verbose:
        print time.asctime(), "Server stop: %s:%s" % (host_name, port_number)

    
