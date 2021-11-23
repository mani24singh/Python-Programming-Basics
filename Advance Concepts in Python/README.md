# Advance Python 1 :
## Exception Handling in Python :
- There are many built-in exceptions that are raised in Python when something goes wrong.
- Exceptions in Python can be handled using a try statement. The code that handles the exception is written in except clause.
- When the exception is handled, the code flow continues without program interruption.

## Raising Exceptions :
- We can raise custom exceptions using the raise keyword in python.

## try with else clause :
- Sometimes we want to run a piece of code when try was successful which can be done using else clause with try.

## try with finally :
- Python offers a finally clause which ensures execution of a piece of code irrespective of the exception.

## if \_\_name_\_ == ’\_\_main_\_’  in Python :
- \__name__ evaluates to the name of the module in Python from where the program is ran.
- If the module is being run directly from the command line, the \_\_name_\_ is set to string “\_\_main_\_”.
- Thus this behavior is used to check whether the module is run directly or imported to another file.

## The global keyword :
- global keyword is used to modify the variable outside of the current scope.

## enumerate function in Python :
- The enumerate function adds counter to an iterable and returns it.

## List comprehensions :
- List comprehensions is an elegant way to create lists based on existing lists.


# Advance Python 2 :

## Virtual Environment :
- An environment that is same as the system interpreter but is isolated from the other python environments on the system.
- Installation : 
   * To use virtual environments, we write ==> pip install virtualenv        ---> #Installs the package
   * We create a new environment using: virtualenv myprojectenv            ----> Creates a new venv
- The next step after creating the virtual environment is to activate it.
- We can now use this virtual environment as a separate python installation.

## pip freeze command :
- pip freeze returns all the packages installed in a given python environment along with the versions.
   - “pip freeze > requirements.txt”
- The above command creates a file named requirements.txt in the same directory containing the output of pip freeze.
- We can distribute this file to other users and they can recreate the same environment using:
   - pip install –r requirements.txt

## Lambda functions :
- Functions created using an expression using the lambda keyword

## bin method(Strings) :
- Creates a string from iterable objects.

## Format method(Strings) :
- Formats the values inside the string into the desired output
    - template.format(p1, p2, …)       ===> #p1, p2 … are the arguments

## Map, Filter & Reduce :
1. **Map** applies a function to all the items in an input_list.
2. **Filter** creates a list of items for which the function returns true.
3. **Reduce** applies a rolling computation to sequential pair of elements. It can be imported as => from functools import reduce












