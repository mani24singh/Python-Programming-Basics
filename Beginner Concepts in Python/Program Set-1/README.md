# Python-Basics-Beginners :
## Print function :
- print(“Hello World”)         # print is a inbuilt python function to print required
   - Execute this file (.py file) by typing python hello.py, and you will see Hello World printed on the screen.

## Modules, Comments & Pip :
### Modules :
- A module is a file containing code written by somebody else (usually) which can be imported and used in our programs.
- - Types of modules : There are two types of modules in Python:
   1. Built-in modules – Pre-installed in Python. Some examples of built-in modules are os, abc, etc.
   2. External modules – Need to install using pip. Some examples of external modules are TensorFlow, flask, etc.
   
### Pip : 
- Pip is a package manager for python. You can use pip to install a module on your system. \
E.g., pip install flask (It will install flask module in your system)
- Using Python as a Calculator : We can use python as a calculator by typing “python” + TO DO on the terminal. [It opens REPL or read evaluation print loop]

### Comments: 
- Comments are used to write something which the programmer does not want to execute. Comments can be used to mark the author's name, date, etc.
- Types of Comments: There are two types of comments in python,
   1. Single line comments – Written using # (pound/hash symbol)
   2. Multi-line comments – Written using ‘’’ Comment ‘’’ or “”” Comment “””.


# Variables and Data Types :
- A variable is a name given to a memory location in a program. 
- Variable – It is a Container to store a value
- Keywords – They are Reserved words in Python
- Identifiers – It is class/function/variable name
- Data Types: Primarily there are the following data types in Python:
   1. Integers
   2. Floating point numbers
   3. Strings
   4. Booleans
   5. None
- Python is a fantastic language that automatically identifies the type of data for us.
> a = 71                  ====>  Identifies a as class<int>
> b = 88.44               ====> Identifies b as class<float>
> name = “Mani”            ====> Identifies name as class<Str>
- Rules for defining a variable name: (Also applicable to other identifiers)
   1. A variable name can contain alphabets, digits, and underscore.
   2. A variable name can only start with an alphabet and underscore.
   3. A variable can’t start with a digit.
   4. No white space is allowed to be used inside a variable name.
- The following are some common operators in Python:
   - Arithmetic Operators (+, -, *, /, etc.)
   - Assignment Operators (=, +=, -=, etc.)
   - Comparison Operators (==, >=, <=, >, <, !=, etc.)
   - Logical Operators (and, or, not)
- type() function : type function is used to find the data type of a given variable in Python.
- Typecasting : A number can be converted into a string and vice versa (if possible). There are many functions to convert one data type into another.
> Str(31)      ===> ”31” Integer to string conversion \
int(“32”)      ===> 32 String to int conversion \
float(32)      ===> 32.0 Integer to float conversion
   - Note :  “31” is a string literal, and 31 is a numeric literal.
   
## input() function : This function allows the user to take input from the keyboard as a string.
> a = input(“Enter name”)        =====> if a is “harry”, the user entered harry \
Note: The output of the input function is always a string even if the number is entered by the user. \
Suppose if a user enters 34, then this 34 will automatically convert to “34” string literal.
