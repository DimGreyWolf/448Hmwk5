# 448Hmwk5
Homework #5, Naa/Nan things

[Homework Assignment Document](http://i.groupme.com/720x960.png.d783d80ae83e49ed9eb518cf2ba9d58e.large)

Homework #5 for EECS 448

# Authors
Harrison Hetler, Henry Nguyen, Tony Nguyen, Lei Wang

# Requirements
This program will require an installation of Python 2.7 and Qt4 to run.
The implementation is written for Python 2.7 and the GUI is implemented
using the Qt4 framework. Graph plotting functionality is provided by
pyqtgraph which requires the previous requirements and NumPy.

To clarify, the list of dependencies are:
* Python 2.7
* Qt4
* NumPy

Most, if not all, these dependencies are usually already installed in your selected OS.

# How to use
To run the program, with a terminal navigate to the folder containing the python scripts.

Then run the command:

`python HW5.py`

This command will then launch the GUI to the program and will prompt you with various functions.

# Using unit tests
There are various unit tests included in this package to verify if certain modules are operating properly. Simply run the "test" prefixed python script associated with the module you would like to test.

For example to test the DrugDatabase module, run:

`python test_drug_database.py`

# MVC Architecture
This program was created with the MVC architecture in mind.
The three main classes of this program are:
* DrugDatabase, which represents the Model class
* DrugGraph, which represents the View class
* DrugAnalysis, which represents the Controller class

Several classes may contain their own subclasses as part of their implementation. NOTE: The DrugGraph class is contained in the executable HW5.py script.

