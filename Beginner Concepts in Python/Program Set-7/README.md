# Functions and Recursions :

## Functions :
- A function is a group of statements performing a specific task.
- When a program gets bigger in size and its complexity grows, it gets difficult for a programmer to keep track of which piece of code is doing what task. Hence, a function can be reused by the programmer in a given program any number of times.
- The syntax of a function looks as follows: 
 > def func(): \
      #code \
This function can be called any number of times, anywhere in the program.

### Function call : Whenever we want to call a function, we put the name of the function followed by parenthesis as follows: 
> func()        =====>  #This is called function call

### Function definition : The part containing the exact set of instructions that are executed during the function call.

### Types of functions in Python : There are two types of functions in Python,
   1. Built-in functions : Already present in Python. eg. includes len(), print(), range(), etc.
   2. User-defined functions : Defined by the user.

### Functions with arguments : A function can accept some values it can work with. We can put these values in the parenthesis. A function can return values as required.

### Default Parameter Value : We can have a value as the default argument in a function.

## Recursion :
- Recursion is a function which calls itself.
- It is used to directly use a mathematical formula as a function. For example: factorial(n) = n * factorial(n-1)
- The programmer needs to be extremely careful while working with recursion to ensure that the function doesn’t infinitely keep calling itself.
- Recursion is sometimes the most direct way to code an algorithm.
