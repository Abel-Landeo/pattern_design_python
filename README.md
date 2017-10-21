# pattern_design_python
Design Pattern of GoF implemented using Python

## Composite Pattern
Representation of objects as tree structures in order to represent part-whole hierarchies. This design pattern focuses on treating individual objects and compositions of objects uniformly.

### When to use it
* Consumers (clients) do not have to be aware between individual objects and compositions of objects; both individual and composite objects are treated uniformly.
* When you need to represent part-whole hierarchies of objects.

### Structure and Elements of Composite Pattern
Normally, Composite Object structure looks like this:

[basic composite structure](https://lh3.googleusercontent.com/kB6I1bP2aqtre4V0QQ7UsYKdwRR6AzpI7U-002Zvwl-JkR46jbKBMkIQ0gZLuYDieZe8jn25B5EzQkc=w1366-h637)

A class diagram to represent this pattern is as follows:

[class diagram of composite pattern](https://lh3.googleusercontent.com/H4QbrLXTK6eIfo71ot4dJPn54OOyD57hM67xphoCzt4WPETX8IVBWs0oPOyWY5MasHK1uIlke0ic1IQ=w1366-h637)
Image taken from GoF Book

Elements of Composite Pattern are:

* __Component__: Interface for objects in the composition, implements default common behavior of all classes and proper access to child components.
* __Leaf__: Individual objects in the composition.
* __Composite__: Defines behavior for composite objects in the composition.
* __Clients__: Consumers that manipulates composite objects through the Component Interface.

### Example 01
We will show employees hierarchy of an organization using composite pattern demo.

Simple class Diagram

[diagram class example 1](https://lh6.googleusercontent.com/Cn6Zg3BOQB7Tyy6-p7k_B-Du3j0gkh5_2TS3FoyRZJV8wk9dSdR4cbuv2d59uQ5dR1hWwaWP3OMGf9Q=w1366-h637)

See implementation in Composite/prog1 folder

### Example 02
We will use a single Shape objects and also a group (composite) of Shapes called Drawing that behaves as a single object.

Simple class Diagram

[diagram class example 2](https://lh3.googleusercontent.com/x01Sf8j45XXnOJr-bjOT8ZT-yEeS7Vxa3hHypO8cAgDoZLqku3L2tve-HQEdH8Ttxc8BNb9da80AxGM=w1366-h637-rw)

See implementation in Composite/prog2 folder
