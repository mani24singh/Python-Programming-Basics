# Notes on Using Virtualenvironment in python:

'''
Virtual-Environment: An environment which is same as the system interpreter
but is isolated from the other python environments on the system.

installation command: pip install virtualenv 

we create a new environment using: 
virtual myprojectenv   ---> to create a new virtual environment

The next step after creating the virtual environment is to activate it. Like Below:

# For MacOS/linux users: source myprojectenv/bin/activate
# For windows powershell users: .\myprojectenv\Scripts\activate.ps1

we can now use this virtual environment as a separate python installation.

while activating the virtualenv if there is a error as virtual script disabled,
then execute --> set.ExecutionPolicy unrestricted -Force in powershell.  [this is more unsafe way which do unleash powers to screw Your system up]
or safe way ---> Set-ExecutionPolicy Unrestricted -Scope Process
# https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows
# https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows



we can use [deactivate] command to come out of the virtualenv in terminal and 
use the system interpreter.
'''

import flask # flask - 0.5.2
import pandas as pd
import pygame


'''
pip freeze command: it returns the package installed in a given python environment
along with the version.
command:   pip freeze > requirement.txt
the above command creates a file named requirement.txt in the same directory
containing the output of pip freeze

we can distribute this file to other users and they can recreate the same
environment using:
pip install -r requirement.txt
'''