"""\
blackboard.py : central key-value store for creating communications servers

This is written using only standard Python modules.

Copyright (c) 2016, Garth Zeglin. All rights reserved. Licensed under the
terms of the BSD 3-clause license as included in LICENSE.
"""

import string
import json
import time
import threading

################################################################
class BlackBoard(object):
    """Define a data store for holding a set of named key-value dictionaries.  This
    class supports writing HTTP servers in various forms to support multi-agent
    communication.  No security is provided, but there are resource limits to
    limit the potential for abuse.  Keys and values may be ASCII or Unicode
    strings; internally they are stored as Unicode.  Access to the data is
    serialized with a lock to support multi-threaded server access.
    """

    def __init__(self):

        # Create Unicode translation mappings for normalizing keys and values.

        # The following mapping converts whitespace into underscores.
        self.key_escape = { ord(ws):ord('_') for ws in string.whitespace }

        # The following mapping where most whitespace is converted to space characters.
        self.value_escape = { ord(ws):ord(' ') for ws in string.whitespace.replace(' ','') }

        # Ordered dictionary of key-value stores, indexed by namespace key.  Each
        # key-value store is a dictionary with string keys and values.  The
        # whole structure is JSON-compatible.
        self.data = dict()

        # Lock to serialize access to self.data.
        self.data_lock = threading.Lock()
        
        # set up the resource limits
        self.max_namespaces   = 30   # maximum number of key-value stores
        self.max_values       = 20   # maximum number of key-value pairs per store
        self.max_key_length   = 20   # maximum length for a namespace or value key
        self.max_value_length = 50   # maximum length for a value string
        
        return

    #================================================================
    def normalize_key(self, key):
        """Normalize a key string into a unicode key with whitespace converted to
        underscores. UTF-8 strings or unicode strings are accepted.  Overly long
        keys are truncated to the maximum length.
        """

        if type(key)==str:
            ukey = unicode(key, 'utf-8')
        else:
            ukey = key

        # truncate overly-long keys
        if len(ukey) > self.max_key_length:
            ukey = ukey[0:self.max_key_length]
            
        return ukey.translate(self.key_escape)

    #================================================================
    def normalize_value(self, value):
        """Normalize a value string into a unicode string with non-space whitespace converted
        to spaces.  UTF-8 strings or unicode strings are accepted.
        """
        
        if type(value)==str:
            uvalue = unicode(value, 'utf-8')
        else:
            uvalue = value
            
        return uvalue.translate(self.value_escape)
    
    #================================================================    
    def write_to_file(self, path):
        """Write the entire database to a file in JSON format."""
        
        with self.data_lock:
            with open(path, "w") as file:
                file.write(json.dumps(self.data, indent = 1))
        return

    def read_from_file(self, path):
        """Replace the current database from the data in a JSON format file."""
        with self.data_lock:
            with open(path, "r") as file:
                self.data = json.loads(file.read())
        return

    #================================================================
    def status_message(self):
        """Return a Unicode plain text status message suitable for providing as a
        default response if no namespace key is provided in the URL.
        """

        return u"""\
message This is a key-value message passing server for Snap! projects.
message The query URL format should be http://<servername>/<namespace>
message The update URL format should be http://<servername>/<namespace>?key1=value1&key2=value2...
num_namespaces %d
max_namespaces %d
max_values %d
max_key_length %d
max_value_length %d
time %s
""" % (len(self.data), self.max_namespaces, self.max_values, self.max_key_length, self.max_value_length, time.time())

    #================================================================
    def data_message(self, namespace):
        """Given a normalized namespace key, return a Unicode plain text key-value
        representation of a particular key-value store.  This may be empty if
        the key is not found.
        """

        with self.data_lock:        
            store = self.data.get(namespace)
            if store is None:
                message = u''
            else:
                message = u''.join([ key + u' ' + value + u'\n' for key,value in store.items()])

        return message
    
    #================================================================
    def _delete_oldest_namespace(self):

        # note: this assumes access is already locked
        
        oldest_timestamp = float("inf")
        oldest = None
        
        for namekey,store in self.data.items():
            timestamp = float(store[u'updated'])
            if timestamp < oldest_timestamp:
                oldest_timestamp = timestamp
                oldest = namekey

        del self.data[oldest]
        return

    #================================================================
    def update(self, namespace, query):
        """Given a normalized namespace identifier and a raw query dictionary, create or
        update a key-value store.
        """

        with self.data_lock:
            store = self.data.get(namespace)

            # create the key-value store if it doesn't exist.
            if store is None:

                # Simple protection against abuse: limit the maximum number of key-value stores.
                if len(self.data) >= self.max_namespaces:
                    self._delete_oldest_namespace()

                # Create a new key-value dictionary.
                store = dict()
                self.data[namespace] = store


            # Save any query key-value pair in the store, following a few limits to
            # help protect against abuse.  Note the text is saved as-is, given that
            # the content type is text/plain, so HTML will just remain text,
            # although some whitespace is normalized to spaces.
            for raw_key,raw_value in query.items():
                value  = self.normalize_value(raw_value)
                key    = self.normalize_key(raw_key)

                # Simple protection against abuse: reset any overly long value
                # strings.  This throws them away and clears the key-value entry
                # rather than truncates so it is obvious they are being dropped.
                if (len(value) > self.max_value_length):
                    value = u''

                if value == u'':
                    # if a blank value was provided, delete any key-value pair from the storage
                    if store.has_key(key):
                        del store[key]
                else:
                    if store.has_key(key):
                        store[key] = value
                    else:
                        # check whether the limit on the number key-value pairs has
                        # been reached, and just drop any additional values
                        if len(store) < self.max_values:
                            store[key] = value                        

            # overwrite particular reserved values
            store[ u'updated'] = unicode(time.time())
                     
        return

################################################################
