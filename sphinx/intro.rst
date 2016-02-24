.. include:: links.rst

Introduction
************

This text is the companion guide to a curriculum for creating performances with
robots.  It is written to be accessible to middle-school students, but could be
used at a variety of levels.

The essential skill is to understand the meaning of movement, action, and form
in context well enough to convey a performance idea via a machine.
Accomplishing this using a robot requires finding insight into performance by
robot proxy as well as learning analytic and programming skills.

The text is written for the `Finch Robot`_ platform sold by `BirdBrain
Technologies`_, and uses the `Snap!`_ visual programming system.  However, the
core ideas are general and this course could be ported to other languages and
robots.


Prerequisites
=============

The text assumes that students are already familiar with the basic use of
`Snap!`_.  Students already familiar with `Scratch`_ may need to study a few of
the additional features provided by Snap.

The exercises assume students are already familiar with these basic programming
ideas in Snap:

#. imperative programming as sequences of commands
#. data representation as numbers and strings (atoms)
#. the idea of composite data representation as lists
#. creating functions with arguments
#. state machine transition diagrams and implementation

And these topics related to robotics:

#. issuing robot commands to change physical state (wheel velocity, LED color)
#. controlling timing of actions using delays
#. sampling robot sensors to estimate physical state (proximity sensors,
   accelerometer)


Learning Goals
==============

The following topics include the essential learning goals related to robot performance:

#. capturing human performance via robot
#. improvising with robots
#. formulating an interaction (pas de deux or dialogue)
#. the role of rhythm
#. ensemble choreography
#. creating meaning through context: story, setting, costuming
#. writing a script for video-recorded performance
#. writing a script for live performance

Accomplishing these objectives will require learning more fundamentals
of robotics including the following:

#. using data to represent actions and trajectories
#. using a networked key-value store
#. using a distributed protocol
#. graphical analysis of the convex hull
#. the definition of uncertainty
#. graphical reasoning about capture regions
#. creating primitives for sensorless navigation
#. designing environmental features for navigational assistance

Implementing these ideas will require new programming skills including the
following:

#. using lists as structured data: arrays, association lists
#. essential functional programming: values, iteration, and mapping
#. understanding recursive functions


Daily Sessions
==============

The course involves a series of hour-long sessions mixing technical exercises to
build robot skills and drama exercises to develop storytelling abilities.  The
course will loosely alternate between technical and drama topics, the exact
schedule is yet to be determined.


Summary of Drama Sequence
-------------------------

#. Introductions, warm-ups, and improv exercises.
#. Storytelling with objects: finding a story in anything, seeing from a new point of view.
#. Storytelling with robots: movement, setting, and relationships.
#. Robot dance party.  Rhythm and synchrony.  Ensemble choreography.
#. Creating a character, finding a voice.
#. Costuming and set design.
#. Robot circus.
#. Developing a theme.
#. Rehearsal skills.
#. Scriptwriting workshop.
#. Practice, practice, practice.
#. Documentation.


Summary of Technical Sequence
-----------------------------

#. Introduction to Snap!
#. State machine programming.  Shared autonomy.
#. Functions, lists, and data.
#. Movement primitives.  Parameterization.
#. Robot geometry.  Diff-drive kinematics, center of rotation, convex hull.
#. Sensorless navigation.  Uncertainty, collisions and capture regions.
#. Ensemble synchronization (networking).
#. Distributed scripting and protocols.
