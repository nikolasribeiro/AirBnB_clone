![imagen airbnb](https://camo.githubusercontent.com/59589bd21e8ec09ef94f2d9bb80d36d144bc487fe4737f8b213d005f3273921b/68747470733a2f2f696d6775722e636f6d2f4f696c457358562e706e67)

                            Welcome to the AirBnB clone project! - The Console 

This is the first part of a project for Holberton School: AirBnB clone - The console. First step: Write a command interpreter to manage the AirBnB objects.

# The command interpreter

First step: Write a command interpreter to manage your AirBnB objects.

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
create the first abstracted storage engine of the project: File storage.
create all unittests to validate all our classes and storage engine

# The command interpreter is currently capable of:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Update attributes of an object
* Destroy an object


# What’s a command interpreter?

A command interpreter is the part of a computer operating system that understands and executes commands that are entered interactively by a human being or from a program.

# Installation

    git clone https://github.com/nikolasribeiro/AirBnB_clone.git
    cd AirBnB_clone

# How to use the interpreter?

    Usage 
    
    interactive mode:

    $ ./console.py
    (hbnb) help

    Documented commands (type help <topic>):
    ========================================
    EOF  all  create  destroy  help  quit  show  update

    (hbnb)
    (hbnb) quit

    ------------------------------------------------------

    Non-Interactive Mode

    echo "help" | ./console.py
    (hbnb) 
    Documented commands (type help <topic>):
    ========================================
    EOF  all  create  destroy  help  quit  show  update

    (hbnb) 

    ------------------------------------------------------

    Example to use a console

    (hbnb) create BaseModel
    228b5b0b-0a25-493b-bf7b-2bb9b7dffe32
    (hbnb) show BaseModel 228b5b0b-0a25-493b-bf7b-2bb9b7dffe32
    [BaseModel] (228b5b0b-0a25-493b-bf7b-2bb9b7dffe32) {'id': '228b5b0b-0a25-493b-bf7b-2bb9b7dffe32', 'created_at': '2021-02-18T18:03:37.393334', 'updated_at': '2021-02-18T18:03:37.393355', '__class__': 'BaseModel'}
    (hbnb) quit



# Files

* models
    * init.py
    * amenity.py
    * base_model.py
    * city.py
    * place.py
    * review.py
    * state.py
    * user.py
    * engine
        * __init__.py
        * file_storage.py
* tests
    * test_models
        * test_engine
            * test_file_storage.py
            * init.py
        * test_amenity.py
        * test_base_model.py
        * test_city.py
        * test_place.py
        * test_review.py
        * test_state.py
        * test_user.py
        * __init__.py
* console.py
* README.md
* AUTHORS

# Commands

    EOF -(Exit command interpreter)
    all - (Displays every instance of class_name, if used without option displays every instance saved to the file)
    create - (Creates an instance of class_name)
    destroy - (Deletes all attributes of class)
    help - (Displays all available commands)
    quit - (Exit command interpreter)
    show -(Displays all attributes of class)
    update - (Updates the key:value of class)

# Environment

Language: Python3
Style guidelines: PEP8

# Authors

* Miguel Crespi | https://github.com/tucucrespi
* Nicolas Ribeiro | https://github.com/nikolasribeiro






