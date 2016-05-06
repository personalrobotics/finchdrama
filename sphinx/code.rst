.. include:: links.rst

.. _code-notes:

Notes on Snap! Sample Code
**************************

Following are notes on each sketch used in the workshop.

Finch-Chrome
============

`Finch-Chrome`_ is the default sketch provided by BirdBrain and loaded by the
Finch Connection App for 'Level 4: Regular Snap!'.  It includes all the Finch
blocks which communicate with the robot, and so is the ancestor of all the other
Finch sketches.

Note that the visible program appears on the Scripts tab for the default Sprite,
and no code appears on the tab for the Stage.  This is recommended so that your
scripts can show debugging information on the canvas using 'say' and 'think',
which can sometimes be helpful.

Finch-Animation-Deck
====================

`Finch-Animation-Deck`_ provides an interface for driving the robot and
recording complex actions into primitives.  It is built using
Finch-Drama-Library.  It can be used as a starting point for creating scripted
performances composed from motion primitives.


Finch-Box-Navigation
====================

`Finch-Box-Navigation`_ is the code used in the :ref:`box-navigation-video`
video.  It uses the plain Finch-Chrome library to implement two different
strategies for navigating around a Finch Box placed on the floor.  It is helpful
to weight the box with something dense and heavy, as the Finch does make
contact.

The first strategy uses the proximity sensors to detect a face, than performs an
open-loop sequence of driving movements to drive around a corner and attempt to
find the next face.

The second strategy adds deliberate collision to reduce positioning error, and works better.


Finch-Coordination-Intro
==================================

`Finch-Coordination-Intro`_ is used in :ref:`exercise-robot-synchronization`.
It uses the plain Finch-Chrome library to implement multi-robot coordination
using communication over a network server.


Finch-Drama-Library
==================================

`Finch-Drama-Library`_ is a reference library to serve as the foundation for
more advanced robot scripting.  It includes a number of new blocks to extend the
basic Finch-Chrome library.  The sketch includes a number of demonstration
scripts on the Stage Scripts tab to test library features.

The library includes the following:

#. A precision teleoperation interface with action recorder.  Keyboard commands
   can be used to puppet the robot while simultaneous building a list data
   structure which can be used for precise playback.

#. Action player to execute action compositions represented as list data.
   Individual actions can be scripted into sequences since actions can invoke
   other actions (non-recursively).

#. Operators to convert action recordings to and from a readable text form.
   This allows extracting action sequences out of Snap for sharing or direct
   editing using a text editor.

#. Object-oriented communications server interface.  The interface maintains
   estimates of client-server clock skew for managing precision synchronization
   of multiple robots.


Finch-Precise-Coordination
==================================

`Finch-Precise-Coordination`_ is a followup to `Finch-Coordination-Intro`_ which
adds an estimation of client-server clock skew, built using the plain
Finch-Chrome library.  It is largely superseded by `Finch-Drama-Library`_ except
as a simpler example for understanding how time works across the network.


Finch-Sensorless-Parking
==================================

`Finch-Sensorless-Parking`_ is used in :ref:`exercise-sensorless-parking`.  It
uses the plain Finch-Chrome library to implement simple open-loop strategies for
using collision with an obstacle for localization.  It isn't autonomous; it
requires user input to initiate the different phases of the movement.


Finch-Sequencing
==================================

`Finch-Sequencing`_ needs to be rewritten to use `Finch-Drama-Library`_, it is
really a precursor to the library and not as capable.  It implements an action
recording and playback system to demonstrate list data structures.  The data is
stored on a per-Sprite basis, which isn't the most obvious to use.


Finch-State-Machine
==================================

`Finch-State-Machine`_ is used in :ref:`exercise-state-machine`.  It implements
a single-loop polled state machine coding structure which can be used to
implement arbitrary state transition graphs.


Sprite-Communication-Intro
==================================

`Sprite-Communication-Intro`_ is used in :ref:`exercise-network-communication`.
It doesn't use the robots; it demonstrates the use of the network communications
server to coordinate graphical sprites across different computers.
