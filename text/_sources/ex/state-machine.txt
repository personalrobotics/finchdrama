.. include:: ../links.rst

Exercise - State Transition Diagrams
====================================

A common problem in Finch programming is switching between sequences of actions
based on human or sensor input.  The simplest case in a linear script sequence
in which each cue simply advances to the next movement.  But as soon as the
robot program start choosing between alternatives, it can be useful to diagram
the logic as a state transition graph.


State Transition Graphs and State Machines
------------------------------------------

The basic idea is that at any given moment, the program exists in one discrete
state, but can transition to other states based on specific conditions.  In the
diagram, states are illustrated as ovals and transitions as directed arcs with
arrowheads.  Each state is a mode with actions defining the behavior in that
state.  Each transition has a predicate, i.e a true-or-false rule, which can be
evaluated based on the sensor and interface inputs and determines whether to
change state.  The combination of the state and transition definitions is known
as a state machine.

There are many possible ways of implementing a given state machine in code.
Diagramming out the logic can help separate the conceptual thinking from the
details of coding.

.. graphviz:: Finch-scripting.dot
	      

State Machine Example
------------------------------

The example state transition graph shown illustrates an exploratory behavior
controlled by the obstacle sensor input and clock time. The basic purpose is to
wander around a space without getting stuck.  Most of the time the Finch drives
forward.  If it sees an obstacle, it enters BACKTRACK to rapidly escape
backwards and then choose a new direction.  If it doesn’t see any obstacles
within a short time, it backs up slightly using REVERSE and randomly changes
direction.  This can help move the Finch away from any obstacles that it cannot
see with its sensors.

Try it out!
-----------

Please try the `sample implementation of the state machine in a Snap sketch
<Finch-State-Machine_>`_.  The code is structured as one large polling loop.  On
each iteration, it evaluates a specific case corresponding to a single state
(e.g. an oval in this graph), applying the actions and deciding whether to
transition.  The current state value is kept as a string in a global variable.
This is an idiomatic programming structure which allows any state to transition
to any other state.

Challenges
----------

#. What failure modes can you observe, e.g., where the robot gets stuck?  Can
   you add states or transitions to avoid this?  Do they create new failure
   modes?
#. How could you use the orientation input to navigate different terrain?
#. Can you simplify the code by creating some new blocks for common operations?
#. Can you make the code more efficient by only issuing each robot command once
   when entering the state?  The example implementation keeps sending the
   identical robot commands again and again, which in many cases is not needed.

*Garth Zeglin, Personal Robotics Lab, Carnegie Mellon University*
