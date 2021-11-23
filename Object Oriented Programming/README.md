# Object-Oriented Programming :
- Solving a problem by creating objects is one of the most popular approaches in programming. This is called object-oriented programming.
This concept focuses on using reusable code. (Implements DRY principle)

## Class :
- A class is a blueprint for creating objects.

## Object : 
- An object is an instantiation of a class. When class is defined, a template(info) is defined. Memory is allocated only after object instantiation.
- Objects of a given class can invoke the methods available to it without revealing the implementation details to the user.     which is referred to as Abstraction & Encapsulation!

## Modelling a problem in OOPs : 
- We identify the following in our problem 
  - Noun -> Class -> Employee 
  - Adjective -> Attributes -> name,age,salary 
  - Verbs -> Methods -> getSalary(), increment()

## Class Attributes : 
- An attribute that belongs to the class rather than a particular object.

## Instance Attributes :
- An attribute that belongs to the Instance (object)

Note: Instance attributes take preference over class attributes during assignment and retrieval.
- example: 
    world.attribute1  \
    Is attribute1 present in the object? \
    Is attribute1 present in class?

## ‘self’ parameter :
- self refers to the instance of the class.
- It is automatically passed with a function call from an object.

## Static method :
Sometimes we need a function that doesn’t use the self-parameter. We can define a static method as @staticmethod decorator.

## __init__() constructor :
- __init__() is a special method which runs as soon as the object is created.
- __init__() method is also known as constructor.
- It takes self-argument and can also take further arguments.


# Inheritance & more on OOPs :
- Inheritance is a way of creating a new class from an existing class.

- Type of Inheritance :
   - 1. Single inheritance
   - 2. Multiple inheritance
   - 3. Multilevel inheritance

### 1. Single Inheritance :
- Single inheritance occurs when a child class inherits only a single parent class.
Base -> Derived

### 2. Multiple Inheritance :
- Multiple inheritances occurs when the child class inherits from more than one parent class.

### 3. Multilevel Inheritance :
- When a child class becomes a parent for another child class.

## Super() method :
- Super method is used to access the methods of a superclass in the derived class.

## Class methods :
- A class method is a method which is bound to the class and not the object of the class.
- @classmethod decorator is used to create a class method.

## @property decorators :
- It is a built in decorator in python which is helpful in defining the properties effortlessly without manually calling the inbuilt function property().

## @.getters and @.setters :
- The method name with @property decorator is called getter method.
- We use getters and setters to add validation logic around getting and setting a value.

## Operator overloading in Python :
- Operators in python can be overloaded using dunder methods.
- These methods are called when a given operator is used on the objects.
- Operators in python can be overloaded using the following methods:
   1. p1 + p2 -> p1.__add__(p2)

   2. p1 – p2 -> p1.__sub__(p2)

   3. p1 * p2 -> p1.__mul__(p2)

   4. p1 / p2 -> p1.__truediv__(p2)

   5. p1 // p2 -> p1.__floordiv__(p2)

## Other dunder/magic methods in Python :
- __str__() -> used  to set what gets displayed upon calling str(obj).
- __len__() -> used to set what gets displayed upon calling .__len__() or len(obj).












