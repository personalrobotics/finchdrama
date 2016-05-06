.. include:: ../links.rst

.. _exercise-primitives:

Exercise - Creating Animation Primitives
========================================

For this individual exercise, we will explore how to practice and record robot
motion sequences which can be composed together.

A recurring idea in robot programming is the use of motion *primitives*, which
are individual actions which be sequenced together to solve a task.  For our
movie performance, each primitive might take the form of a short dance step or
phrase, or a individual reaction movement responding to another character.


Try it!
-------

We will use the `Finch-Animation-Deck`_ sketch for this exercise.  This example
uses Finch-Drama-Library to implement an animation interface which allows
recording individual primitives using a driving interface, then saving them as
named primitives in a stored library.  These primitives can then be replayed by
name.

The comments in the sketch should guide through testing all the features as follows:

#. Clearing the library to erase all stored primitives.
#. Driving the robot using the keyboard.
#. Choosing a name for a new primitive, then performing and saving it.
#. Replaying actions by name.

   
Building a Performance
----------------------

#. First, decide on a basic story context and the role of your robot character.
#. Try improvising robot movement to see what kinds of actions might be consistent with this character.  Are they fast, slow, staccato, smooth?
#. Try some short general-purpose expressions; can you animate a double-take?  Surprise?  Fear?
#. When you are happy with a movement, choose a name and save it.
#. Try programming a sequence using normal Snap! techniques and the ``play action "" from library []`` command block to execute your primitives.

*Garth Zeglin, Personal Robotics Lab, Carnegie Mellon University*
