![imagen airbnb](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210218%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210218T195758Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=08f094e55735d5c2e9fbb7d27c8af832033eb5e1efd5dd60dca43a81c4cfa575)

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

* Miguel Crespi |
* Nicolas Ribeiro |






