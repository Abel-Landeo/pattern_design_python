# pattern_design_python
Design Pattern of GoF implemented using Python

## Composite Pattern
Representation of objects as tree structures in order to represent part-whole hierarchies. This design pattern focuses on treating individual objects and compositions of objects uniformly.

### When to use it
* Consumers (clients) do not have to be aware between individual objects and compositions of objects; both individual and composite objects are treated uniformly.
* When you need to represent part-whole hierarchies of objects.

### Structure and Elements of Composite Pattern
Normally, Composite Object structure looks like this:

[basic composite structure](https://drive.google.com/open?id=0B1I420fBHITvTzFpcHZkV25Mc1E)

A class diagram to represent this pattern is as follows:

[class diagram of composite pattern](https://drive.google.com/open?id=0B1I420fBHITvc1p5X0F1WmNuWTQ)
Image taken from GoF Book

Elements of Composite Pattern are:

* __Component__: Interface for objects in the composition, implements default common behavior of all classes and proper access to child components.
* __Leaf__: Individual objects in the composition.
* __Composite__: Defines behavior for composite objects in the composition.
* __Clients__: Consumers that manipulates composite objects through the Component Interface.

### Example 01
We will show employees hierarchy of an organization using composite pattern demo.

Simple class Diagram

[diagram class example 1](https://drive.google.com/open?id=0B1I420fBHITvZ2pIVWNITUdBOG8)

See implementation in Composite/prog1 folder

### Example 02
We will use a single Shape objects and also a group (composite) of Shapes called Drawing that behaves as a single object.

Simple class Diagram

[diagram class example 2](https://drive.google.com/open?id=0B1I420fBHITvTnJfM2pDTE5na2M)

See implementation in Composite/prog2 folder
