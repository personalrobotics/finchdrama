#!/usr/bin/env python
"""\
flask_server.py : wsgi communications server for Snap! sketches

This is written using the Flask framework.

Copyright (c) 2016, Garth Zeglin. All rights reserved. Licensed under the
terms of the BSD 3-clause license as included in LICENSE.
"""

from flask import Flask
from flask import Response
from flask import request

# single global storage object
import blackboard
bb = blackboard.BlackBoard()

# main application
app = Flask(__name__)


@app.route("/<namespace>")
def query(namespace):

    # The base of the URL specifies which key-value store to address.
    ns = bb.normalize_key(namespace)

    # Each query elements will update an entry, or delete one if the value is empty.
    bb.update(ns, request.args)

    # Create a plain text response with a single key-value pair per line.
    server_fields = u"namespace " + namespace + "\n"
    response = Response(bb.data_message(ns)+server_fields, mimetype="text/plain")

    # The following header field will specifically allow Javascript loaded from
    # the Snap! site to access this resource. For details, see: http://enable-cors.org/server.html
    response.headers.add( 'Access-Control-Allow-Origin', 'http://snap.berkeley.edu')
    return response


@app.route("/")
def empty():
    response = Response(bb.status_message(), mimetype="text/plain")
    response.headers.add( 'Access-Control-Allow-Origin', 'http://snap.berkeley.edu')
    return response

if __name__ == "__main__":
    app.run()
