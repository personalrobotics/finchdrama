.. include:: ../links.rst

Exercise - Robot Synchronization
================================

For this exercise, we will try coordinating the performance of several Finch robots.

Coordinating Multiple Robots
----------------------------

One student should assume the role of ‘director’.  Their task is to send
messages when the performance begins and at each script mark.  In this example
there are four script points, each associated with a specific behavior.

The other students will allow their robots to be controlled by the director.  At
each script change event, a different sequence will be triggered on their robot.
However, the director can only indicate the start of a sequence, the actual
behavior is up to the individual programmer.

Try it out!
----------------------------

Before we go further in the discussion, let’s try this.  The `example sketch
demonstrates communication <Finch-Coordination-Intro>`_ to synchronize the
robots.  It includes both the director and actor scripting.  Please read the
comment in the Snap sketch and try out the steps to see how network
communication works.


Discussion
----------------------------

If you have followed the notes in the sketch, then you should have been able to
see multiple robots performing a few movements, colors, and melodies in
approximate synchrony.

Note that there is a fair amount of timing ambiguity since each robot is only
polling the server once per second, but executing each script change as soon as
it is received.  There can be more than a second of difference between the
timing of different robots.


Terminology
----------------------------
There are several terms which will help us in future discussion.


Code Commentary
----------------------------


Challenges
----------------------------

#. Can you design new choreography for each phase of the script?  How do they look performing alongside the other robots?


*Garth Zeglin, Personal Robotics Lab, Carnegie Mellon University*
