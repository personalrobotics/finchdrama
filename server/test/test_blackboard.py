# -*- coding: utf-8 -*-

# Unit test script.

# To use, run the following from the parent directory:
#   nosetests -v

from __future__ import print_function

from nose.tools import assert_equal, assert_in, assert_is

import blackboard

def test_blackboard_ascii():
    namespaces = ["abc", "def"]
    data = { 'x':'1', 'y':'2' }
    
    bb = blackboard.BlackBoard()
    for ns in namespaces:
        bb.update(ns, data)

    for ns in namespaces:
        msg = bb.data_message(ns)

    bb._delete_oldest_namespace()
    
def test_blackboard_unicode():
    namespaces = [u"abc", u"def", u"uni€ÂĎÌṀǽ✪"]
    data = { u'x':u'1', u'y':u'2', u's':u'©', u'§':u'◉' }
    
    bb = blackboard.BlackBoard()
    for ns in namespaces:
        bb.update(ns, data)

    for ns in namespaces:
        msg = bb.data_message(ns)
        # print (msg.encode('utf-8'))
        
    bb._delete_oldest_namespace()


