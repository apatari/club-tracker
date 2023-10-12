
# Club Tracker - A database management CLI

This is a command line interface (CLI) designed to manage a many-to-one relationship between students who are each enrolled in one of the school clubs.  With some modification of prompts and table names, the functions and menu system can work to manage any database with a similar many-to-one relationship between two classes.

## Setup

In order to use this app on your own machine, first make sure you have Python and pipenv installed on yor computer.  From there fork fork and clone this repository and run the following commands in the club-tracker directory to enter the virtual environment:

```bash
pipenv install

pipenv shell
```
Change into the /lib directory and run the CLI:

```bash
cd lib

python cli.py
```

## Usage

![](https://github.com/apatari/club-tracker/blob/main/CLIMainMenu.png) 

A series of menus will prompt you with the operations you can run.  Type the appropriate letter or number to navigate menus or select the operations to carry out.  Menu and value entries are case sensitive.  Actions the program can can carry out include creating, updating, and deleting students and clubs, viewing all clubs or students, and finding students by club or name.   

## Files and functions

In the /lib folder, you'll find the cli.py file which contains the menus and display functions.  As noted above, executing this file within the /lib directory will run the CLI tool.  

Also in the /lib directory is helpers.py.  This file contains the functions that connct the user interface to the database and the Python classes that represent each table.  The functions themselves have names that describe their purpose, such as add_club or update_student.  

The file debug.py is a tool that allows testing during the development process.  Executing this file will enter a debugging prompt.  It is not necessary for use of the CLI, but may be handy for anyone modifying the program's behavior.  Currently it creates a few variables which point to clubs and students in the database for easier access while using the debugger.  Make sure there are at least a few clubs and students in the database before running debug.py otherwise it will throw an error.  Running seed.py will fix this quickly. 

Speaking of seed.py, this program erases the existing database and repopulates it with sample code for testing.  DO NOT run seed.py unless you intend to discard all data currently in the database.  The current file will leave a database with three clubs and four students.

In the models folder, __init__.py creates the cursor and connection to the database.  You'll see it imported by other files that need to perform SQL based actions on the database.  The two models in that folder, club.py and student.py each contain the functions necessary to initialize, validate, and maintain instances of each class, as well as the tables themselves.  Other methods provide functionality such as counting or returning the number of students in a club.

## Acknowledgment

Thanks to the folks who created and maintain [pipenv](https://pipenv.pypa.io/en/latest/) and the [Rich library for Python](https://rich.readthedocs.io/en/stable/introduction.html)




---
