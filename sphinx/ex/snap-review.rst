.. include:: ../links.rst

Exercise - Review of Snap!
==========================

Snap! is a browser-based graphical programming language used for all the robot
programming activities in this workshop.  Ideally students will already be
familiar with Snap! (see :ref:`prerequisites`) but the following is a guide to
quickly learning enough of the system to get started.


Basic Concepts
--------------

`Snap!`_ is a drag-and-drop block-based language created at UC Berkeley as an
improvement on `Scratch`_.  Programs are constructed by dragging blocks
representing computational operations into stacks.  The blocks have exterior and
interior shapes which indicate the kinds of functions they perform. The system
will only allow blocks to fit together which have compatible properties.  E.g. a
block with a slot expecting a true or false input value has a hexagonal shape;
blocks which produce a true or false value have a hexagonal exterior and will be
allowed to fit into the slot.  Note that doesn't mean the program will work,
just that all programs which can be drawn are syntactically correct and can be
evaluated.

The usual application of Snap! is writing interactive graphical programs which
draw sprite and pen graphics in a browser canvas and make sounds.  The Snap!
support for the Finch robots adds additional blocks which communicate with the
robot hardware.  Most of the drawing and sound operators will not be used in
this course since we will focus on robot performance.

The important improvements of Snap! over Scratch can be summarized as follows:

#. Support for cloud storage of sketches.  The ScratchX system used with the
   Finch does not have access to the community cloud system, so it is difficult
   to share sketches.  Note, however, that Snap! does not have a community
   portal, just a cloud server, but users may pass out their own links to
   sketches they make public.

#. Support for recursion in user-defined blocks.

#. First-class data lists.  Together with recursion, this opens the door to many
   programming techniques, including structured data manipulation and
   object-oriented design.

#. Implementation in Javascript instead of Flash (more broadly compatible with
   new devices, more future-proof).

Online Resources
----------------

The course guide includes the following Snap! resources:

#. :ref:`All sketches associated with this course are described in the code notes.<code-notes>`
#. :ref:`Quick reference guide to the standard Snap! and Finch blocks<snap-reference>`
#. :ref:`Reference guide to the course Snap! library<course-library>`

The following general resources are available from BirdBrain and UC Berkeley:

#. `BirdBrain Finch and Snap guide <Finch Chromebook Support_>`_
#. `BirdBrain Snap! tutorial`_
#. `BirdBrain Snap! library <Finch-Chrome_>`_ (direct link to interactive system)
#. `Snap! interactive system (i.e. without Finch) <run Snap!_>`_ (direct link to interactive system)
#. `Snap! official reference manual <Snap Manual_>`_
#. `Snap! source code`_


Agenda for Review
-----------------

Your instructor will guide you through the following topics and terminology:

#. Starting Snap!

   #. For Snap! alone: `run Snap!`_
   #. With the Finch, start the Finch Connection App first.

#. Saving your sketches.

   #. Creating a cloud account from within Snap! so you can work on sketches from any computer.
   #. Saving both locally and on the cloud.
   #. Setting cloud sketches to be public.
   #. Note: Finch-based sketches can still be loaded and run even if no robot is
      attached, although any robot-related output operations will have no effect
      and sensor operations will return default values.  This can be useful for
      offline testing.

#. Basic block types and terminology:

   #. Hat blocks.
   #. Command blocks.
   #. Reporter blocks (oval).
   #. Predicate blocks (hexagon).
   #. C-shaped blocks.

#. Control flow through blocks.

#. Atomic data types:

   #. Numbers.
   #. Booleans.
   #. Strings.

#. Finch command and reporter blocks.

   #. Robot output commands.
   #. Sensor reporters.

#. Controlling timing and delay.

#. Global variables.

#. Script variables.

#. Lists.

#. Threading and concurrent execution.

#. Defining new blocks.

   #. Arguments.
   #. Return values.
   #. Recursion.

#. Using block libraries.

#. Reading code defined within Snap!.
