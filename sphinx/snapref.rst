.. include:: links.rst

.. _snap-reference:

Standard Snap Blocks Reference
******************************

The `Snap Manual`_ details many of the operators provided in the language but is
not comprehensive.  The following reference is intended to provide a quick guide
to every standard operator in the native set as well as a few of the libraries.


Key to Block Descriptions
=========================

Standard library
  Includes the primitive blocks always available in `Snap!`_.

Tools library
  These blocks are available once **Import Tools** is run from the File menu.

Finch library
  The blocks in the BirdBrain Finch-Chrome library, which can found in the Snap
  sketch loaded by the `Chrome Finch Connection App`_.


Key to Block Arguments
----------------------

The argument notation is idiosyncratic, but follows this convention:

=======	===============================================
Symbol	Data Type
=======	===============================================
``#``	numeric value
``<>``	Boolean value
``""``	string
``[]``	list
``*``	general value (text or string)
``&``	name of variable, sprite, operation, etc.
``()``	procedure
``[%]``	color (selected from color picker)
``...``	variable number of arguments
=======	===============================================


Key to Block Shapes
-------------------

===============	===============	====================================================
Shape		Category	Properties
===============	===============	====================================================
C-shaped	special form	accepts one or more procedures within the body
oval		reporter	returns a value
tabbed		command		called for side-effects (no return value)
hexagon		predicate	returns a Boolean value
hat		entry point	starts a thread of execution, i.e., a script
cap		exit point	ends a thread
===============	===============	====================================================


Table of Blocks
===============

.. csv-table::
   :header-rows: 1
   :widths: 8,8,6,8,25,25,50
   :file: snap-reference.csv
