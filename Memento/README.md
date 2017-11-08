#Memento
Based on GoF 1994 Book

##What is this pattern for?
This pattern pretends capture and externalize some object's internal state and then restore this state later on.

This pattern does so without violating encapsulation.

##Motivation
Sometimes users need to go back to previous steps, or restore changes when they make mistakes.

Due to encapsulation, states are inaccessible and it is impossible to save states externally. On the other hand, exposing states violates encapsulation and the application's reliability and extensibility are compromised.

##When to use it
* Obtaining the state of an object directly would expose implementation details and break the object's encapsulation.
* A snapshot of (or part of) an object's state must be saved in order to restore it to that same state later.

##Structure and Elements of Memento Pattern
Based of GoF, the OMT for Memento is as follows:

[Basic Memento structure](https://drive.google.com/open?id=1CKT8pAod-xgHBJv72AWZCtkrsNJPrawp)

Elements of Memento Pattern are:
* __Memento (SolverState)__: Stores internal state of the Originator object. Prevent access from objects othen than the originator.
* __Originator (ConstraintSolver)__: Snapshots the current internal state and save it creating a memento; uses the memento to restore its internal state.
* __CareTaker (undo mechanism)__: Never operates on or examines the contents of a memento; provides safekeeping for the memento.

##Collaborations
As shown in the following pic taken from the GoF Book

[collaboration memento pattern](https://drive.google.com/open?id=1_IS63QhQsmshpjcDJWWouvuXUu4L9IZ8)

##Demo 01
We will show an object changing their internal state and we'll store some states and later restore them using Memento Pattern.

Class Diagram:

[class diagram demo 01](https://drive.google.com/open?id=1FBIIjYcTLYFrYk9mgcvNX-9v0rHACfbn)

See implementation in Memento/prog1
