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

# Short Definitions of the rest of Pattern Designs (PD):
## Creational PDs:
* __Singleton__: For creating only one instance of a class and providing only one global access to that instance.
* __Prototype__: For cloning another object when the creation of that object is costly or takes many Database hits; the cloning process can be shallow copy or deep copy.
* __Factory__: For creating specialized instances from a Base class based on some rules or criteria; the class that encapsulates this criteria is called Factory Class and it hides the creational procedure to the client or consumer.
* __Abstract Factory__: For creating family of instances of objects. This DP is also called Factory of Factories; the class that gets one or another Factory is called Abstract Factory Class.
* __Builder__: For creating objects based on a corresponding step-by-step procedure per object to be created. The class that contains the procedures is called Builder Class and it hides this procedures to the clients or costumers.

## Structural PDs:
* __Adapter__: For connecting two incompatible interfaces. This Pattern use a Wrapper class on the incompatible interface in order to provide a compatible interface.
* __Bridge__: For decoupling an abstraction from its implementations so that both can vary independenty meaning that both classes can be altered structurally without affecting each other.
* __Composite__: See above for complete detail.
* __Decorator__: For adding new functionality to an existing object dinamically meaning that the class structure of the object is not altered.
* __Facade__: For providing a unified interface for a set of interfaces in a complex subsystem. The purpose is to hide complexities of a system to the clients or consumers by showing simplified methods in one interface called Facade.
* __Flyweight__: For reducing the number of objects created in order to reduce memory footprint and improve performance. This PD reuses already created objects to provide similar objects and a new object will be created only if there is no similar object created yet.
* __Proxy__: For providing a class which represents functionalily of another class so that the cost of fully creation of the object can be controlled.

