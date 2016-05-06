.. include:: links.rst

.. default-domain:: js

.. _course-library:

Drama Library Blocks Reference
******************************

The `course library <Finch-Drama-Library_>`_ is a common set of Snap blocks used
across many of the exercises.  They will likely be useful for student projects
as well as example code for highlighting programming techniques.  This library
is built using the standard Snap blocks described on the :ref:`snap-reference`
page and follows the same conventions.


Summary of Library
==================

.. csv-table::
   :header-rows: 1
   :widths: 6,8,6,8,25,25,50
   :file: lib-reference.csv

Detailed Documentation
======================

This section includes usage documentation and design discussion for the library
blocks.

.. _data-structures:

Data Structures and Special Values
----------------------------------

All data structures in Snap are built from lists and atomic values such as
integer, text, Boolean, or procedure.  So different 'types' in most cases are
really usage conventions.

association-list
  An association list is a list of two-element lists, each containing a key and
  a value, with each key appearing no more than once.  It implements a
  dictionary or associative memory, mapping keys to values. [#alist]_

action-list
  An action list is a variable-length list used to represent a single
  output to the robot with an optional duration.

recording-list
  A list of action-lists, representing a time-series of outputs to the robot.

action-library
  An association list mapping action names to recording lists.  The
  recording lists may also include a special ``call *`` action to allow one
  action sequence to include another.

server-descriptor
  A list encapsulating all the state for a server channel: the URL, channel
  (namespace) identifier, estimated clock skew, most recently transmitted query,
  and most recently received response.

null
  An empty value distinct from any other value, conceptually representing
  'None'.  This value can be returned using a ``report`` operator with
  no value.  It is *not* the same as an empty list.  The ``is * identical to *
  ?`` operator reports it as identical to an empty box.  The ``is * a &?``
  operator reports true for number, and the ``length of ""`` operator reports
  zero.  The library provides ``null? *`` to test for this value.

.. [#alist] An association list value can be a list, but since improper lists (dotted pairs) are not supported, each entry still has only two elements, the second of which is a list.

Association Lists
-----------------

``null? *``
   Returns true if the value is equivalent to an empty value, else false.

``find value for * in a-list []``
   Search the association list for the given key.  Returns just the value, or null if not found.

``find record for key * in a-list []``
   Search the association list for the given key.  Returns the [key, value] list, or null if not found.

``set value * for key * in a-list []``
   Replace the value for the given key in the association list, adding it if not present.

``for each &key &value of a-list []``
   Iterate over each [key, value] pair in the association list, calling the
   procedure in the body of the C-shaped block with the local variables set to a
   key and a value.

Driving and Recording
---------------------

``drive Finch and record into []`` Runs keyboard-driving interface, recording an action-list for each change of output into an existing list.
  The list may be empty to begin, but must exist in order to be modified.  If no
  list is provided, then the block just runs the teleoperation interface without
  recording.  The default key bindings are as follows.  Note that the movement
  keys superimpose; pressing the right arrow while holding down the up arrow
  creates a curving arc.

    =====	==============  
    key		action
    =====	==============
    up		forward
    down	reverse
    left	turn CCW in place
    right	turn CW in place
    1		set 25% speed
    2		set 50% speed
    3		set 75% speed
    4		set 100% speed
    x           exit driving teleoperation loop
    =====	==============  
  

``drive LEDs and record into []``
  Runs keyboard-controlled lighting interface, recording events into the given
  recording list.

``drive buzzer and record into []``
  Runs musical keyboard interface, playing notes on the Finch buzzer and
  recording events into the given recording list.  The keyboard is sampled at a
  fraction of the current tempo so all notes are quantized according to the
  tempo.

Sound
-----

``Finch buzz MIDI note # for # beats``
  Play a musical note of a given duration on the Finch buzzer.  Note that the
  underlying primitive accepts a duration in milliseconds, so this block
  computes the duration from beats using the current global tempo setting.  The
  note length is implemented on the Finch itself; this block does not execute
  any delay, but returns immediately.  The note is specified as a standard MIDI
  note integer.  Each integer value represents a musical half-step, so for
  example, middle-C is 60, C# is 61, the tuning A (440Hz) is 69, and the C an
  octave above middle C is 72.
  

Action Libraries
-----------------

``play Finch action []``
  Interpret and perform a single action represented as an action-list, including
  delay for duration.  This may set the motor speed, change the LED color, or
  play a note on the buzzer.

``play action "" from library []``
  Play a named action sequence from the given action library.  The special
  ``call`` action is allowed to recursively invoke other actions from the same
  library, so this can be used to create a hierarchy of script sequences.  Care
  should be taken to avoid recursive calls since there are no conditionals to
  end recursion.
  
``action library -> text []``
   Print an action library into a text form.  This allows a readable script to be saved in a text variable and exported to an external file.  Returns a string.

``text -> action library ""``
   Parse a text representation of an action library and returns an action library.
  

Networking
----------

The communications server supports sharing sets of key and value pairs on a
number of distinct *channels* or *namespaces*.  The networking functions use a
server-descriptor (see :ref:`data-structures`) to encapsulate all the state for
a connection to simplify the interface for sending and receiving messages.
Messages are sets of key-value pairs, i.e., a message is an association list.

``descriptor for server "" channel *``
  Create a new descriptor object given a server hostname and a namespace
  identifier. All robots in the same performance group will need to specify the
  same channel name.  It is recommended to use your own channel name to avoid
  crosstalk with other groups.

``poll server []``
  Fetch the current state of a server channel as an association list.
  
``send message list [] via server []``
  Send an association list of key-value pairs to update the server state,
  returning an association list with the new state.

``send cue * with # seconds delay``
  Send a message with ``next_cue`` and ``start_time`` fields to indicate an
  event in the future.  The time is sent as an absolute timestamp measured
  against the server clock.  This allows clients to adjust the command to their
  own local clocks using their individual skew estimations

``clock skew for server []``
  Retrieve the clock skew estimate from the server descriptor.  This represents
  the number of seconds by which the local time is ahead of the server time.  If
  the value is negative, the local time is behind.  This estimate is adjusted
  during each server transaction.


Utility Functions
-----------------

``current time``
  Returns the current local clock time in seconds to millisecond precision.
  This is 'epoch' time, the number of seconds since midnight of January 1, 1970.
