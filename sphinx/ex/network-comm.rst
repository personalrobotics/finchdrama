.. include:: ../links.rst

Exercise - Network Communication
================================

For this exercise, we will explore a method for coordinating several Snap sketches using
communication over a network.

Coordinating Multiple Robots
----------------------------

Programming multiple robots to work together requires coordinating their
actions.  This can be as simple as taking turns or as complex as combining
sensor information from multiple robots.  Timing is essential to dramatic
performance, so it can be important to synchronize multiple robot actors tightly
to move together or precisely take turns.

The simplest way to accomplish coordination is for humans to act as the eyes and
ears of the robots and puppet them using keyboard commands, but it would be
useful to automate elements of a performance.  The Finch has very limited
capabilities to physically communicate from robot to robot, but the control
computers can much more easily pass messages back and forth using the network.

Try it out!
-----------

Before we go further in the discussion, let’s try this.  The `first example
sketch <Sprite-Communication-Intro>`_ demonstrates communication to control
graphic sprites without needing any robots.  Please read the comment in the Snap
sketch and try out the steps to see how network communication works.

Discussion
----------

If you have followed the notes in the sketch, then you should have been able to
see that a set of (key, value) pairs can be shared among multiple computers
using a server as an intermediary.

The complications of controlling robots with this approach revolve around
carefully choosing what kind of data will be sent and by which robots.  It takes
time for each query, so the server can only be polled at a modest rate, no more
than a few times a second.  The amount of data is limited to a few sets of
numbers or strings.

However, the robots can each be preprogrammed with script sequences, so the
actual movements don’t need to be sent.  The controlling computer need only act
as a kind of conductor or director and indicate only which section to run and
when.  Since each computer has a local clock, this instructions can also specify
actions to take place in the near future so each robot has time to fetch the
current directions.  We will see some of this in the next exercise with actual
robots.

Terminology
-----------

There are several terms which will help us in future discussion.

**Key and Value**. A key is a kind of name, a text string used to identify a
piece of data, i.e. a value, in a database.  This approach is commonly called a
`key-value store`_ or key-value database.  In this example, the ‘value’ is a text
string which can encode a set of numbers or strings.

**Blackboard**.  A physical blackboard has the property than anyone in the room
can write on it, and anyone can read it.  A `blackboard system`_ is a programming
idiom for using a common memory for coordinating multiple computers or programs.
The communication system in this exercise can be considered a kind of online
blackboard.

Code Commentary
---------------

It is instructive to examine the details of the [process message] command block.
If you right-click on an instance, you can select **edit..**  to see the code.

The main structure is a **for-each-of** loop which iterates once for each line of
text from the server response.  The **split** operator is used to divide the
response text into a list of strings, one per line.  On each iteration of the
loop, the line script variable holds one text line.

This line is divided again with **split**, this time dividing the line at each
space into a list of strings, and storing the result in **record**. The first
item in this list is the key string, stored in **key**.  The list of one or more
value items is stored in **value**.  The number of value items depends upon the
data format for the given key; in this example, most values have only a single
item, but the **xy_position** value is a pair of numbers.

Following this data dissection is a set of **if-then-else** commands to
determine what to do with the key-value pair.  In this example, each outcome is
simply to store the value data in a particular global variable, but other
actions are also possible such as immediately issuing a robot command.

Note that the keys can come from the server in any order and may include
unrecognized new keys.  This scheme handles these cases without breaking.

Challenges
----------

#. Can you add a new key-value pair to the blackboard?  Be sure to update the
   [process message] block to correctly interpret the value.

*Garth Zeglin, Personal Robotics Lab, Carnegie Mellon University*
