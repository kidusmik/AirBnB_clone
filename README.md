# Team Project - AirBnB Clone

This is ALX/Holberton's project *AirBnB Clone*, as the title states it is cloning the AirBnB web application leading owards building full web application: the *AirBnB Clone*

## Project Description

This project is building a terminal that is used to test important objects of the project, the tests include:

* Creating the object
* Destroying the object
* Displaying the specific object
* Destroying the object
* Diplaying all the objects created
* Updating the object

### Classes

| Name | Description |
| --- | --- |
| BaseModel | Defines all common attributes/methods for other classes |
| --- | --- |
| FileStorage | Serializes instances to a JSON file and deserializes JSON file to instances |
| --- | --- |
| User | Holds user information |
| --- | --- |
| State | Holds state information |
| --- | --- |
| City | Holds city information |
| --- | --- |
| Amenity | Holds amenity information |
| --- | --- |
| Place | Holds place information |
| --- | --- |
| Review | Holds review information |
|--- | --- |

## The Command Interpreter

The command interpreter is used to perform actions to objects of the classes mentioned above.

### Starting the Terminal

To run the command interpreter, execute the `console.py` file.

```
kidusmik@ubuntu$ ./console.py
(hbnb) 
```

### Usage

There are list of commands that can be interpreted by the terminal.

| Command | Syntax | Function |
| --- | --- | --- |
| create | `create <class name>` | Creates a new instance of the class |
| --- | --- |
| show | `show <class name> <id>` | Prints the string representation of an instance based on the class name |
| --- | --- |
| destroy | `destroy <class name> <id>` | Deletes an instance based on the class name and id |
| --- | --- |
| all | `all` or `all <class name>` | Prints all string representation of all instances based or not on the class name |
| --- | --- |
| update | `update <class name> <id> <attribute name> <attribute value>` | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file |
| --- | --- |

### Example

Here are some examples of the terminal usage.

```
kidusmik@ubuntu:~AirBnB_clone$ ./console.py
(hbnb) create BaseModel
ae76953c-4f05-4e14-9659-e599cd45a229
(hbnb)
(hbnb) create Place
4e70b774-e1ce-45c6-8993-45e10ce48a46
(hbnb)
(hbnb) show BaseModel 4e70b774-e1ce-45c6-8993-45e10ce48a46
** no instance found **
(hbnb)
(hbnb) show BaseModel ae76953c-4f05-4e14-9659-e599cd45a229
[BaseModel] (ae76953c-4f05-4e14-9659-e599cd45a229) {'id': 'ae76953c-4f05-4e14-9659-e599cd45a229', 'created_at': datetime.datetime(2022, 1, 26, 19, 50, 46, 400369), 'updated_at': datetime.datetime(2022, 1, 26, 19, 50, 46, 400501)}
(hbnb)
(hbnb) create NonExistingClass
** class doesn't exist **
(hbnb) create
** class name missing **
(hbnb) show
** class name missing **
(hbnb) show NonExistingClass
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) destroy BaseModel
** instance id missing **
(hbnb)
(hbnb) all
["[BaseModel] (ae76953c-4f05-4e14-9659-e599cd45a229) {'id': 'ae76953c-4f05-4e14-9659-e599cd45a229', 'created_at': datetime.datetime(2022, 1, 26, 19, 50, 46, 400369), 'updated_at': datetime.datetime(2022, 1, 26, 19, 50, 46, 400501)}", "[Place] (4e70b774-e1ce-45c6-8993-45e10ce48a46) {'id': '4e70b774-e1ce-45c6-8993-45e10ce48a46', 'created_at': datetime.datetime(2022, 1, 26, 19, 50, 49, 59166), 'updated_at': datetime.datetime(2022, 1, 26, 19, 50, 49, 59232)}"]
(hbnb)
(hbnb) destroy BaseModel ae76953c-4f05-4e14-9659-e599cd45a229
(hbnb)
(hbnb) all
["[Place] (4e70b774-e1ce-45c6-8993-45e10ce48a46) {'id': '4e70b774-e1ce-45c6-8993-45e10ce48a46', 'created_at': datetime.datetime(2022, 1, 26, 19, 50, 49, 59166), 'updated_at': datetime.datetime(2022, 1, 26, 19, 50, 49, 59232)}"]
(hbnb)
(hbnb) create BaseModel
c37c1765-bd84-4890-90b4-690afffb2b3d
(hbnb)
(hbnb) all
["[Place] (4e70b774-e1ce-45c6-8993-45e10ce48a46) {'id': '4e70b774-e1ce-45c6-8993-45e10ce48a46', 'created_at': datetime.datetime(2022, 1, 26, 19, 50, 49, 59166), 'updated_at': datetime.datetime(2022, 1, 26, 19, 50, 49, 59232)}", "[BaseModel] (c37c1765-bd84-4890-90b4-690afffb2b3d) {'id': 'c37c1765-bd84-4890-90b4-690afffb2b3d', 'created_at': datetime.datetime(2022, 1, 26, 19, 54, 52, 766133), 'updated_at': datetime.datetime(2022, 1, 26, 19, 54, 52, 766219)}"]
(hbnb) all BaseModel
["[BaseModel] (c37c1765-bd84-4890-90b4-690afffb2b3d) {'id': 'c37c1765-bd84-4890-90b4-690afffb2b3d', 'created_at': datetime.datetime(2022, 1, 26, 19, 54, 52, 766133), 'updated_at': datetime.datetime(2022, 1, 26, 19, 54, 52, 766219)}"]
(hbnb)
(hbnb) update
** class name missing **
(hbnb) update BaseModel
** instance id missing **
(hbnb) update BaseModel 4e70b774-e1ce-45c6-8993-45e10ce48a46
** no instance found **
(hbnb) update BaseModel c37c1765-bd84-4890-90b4-690afffb2b3d
** attribute name missing **
(hbnb) update BaseModel c37c1765-bd84-4890-90b4-690afffb2b3d email
** value missing **
(hbnb) update BaseModel c37c1765-bd84-4890-90b4-690afffb2b3d email "kidusmik@gmail.com"
(hbnb)
(hbnb) all
["[Place] (4e70b774-e1ce-45c6-8993-45e10ce48a46) {'id': '4e70b774-e1ce-45c6-8993-45e10ce48a46', 'created_at': datetime.datetime(2022, 1, 26, 19, 50, 49, 59166), 'updated_at': datetime.datetime(2022, 1, 26, 19, 50, 49, 59232)}", "[BaseModel] (c37c1765-bd84-4890-90b4-690afffb2b3d) {'id': 'c37c1765-bd84-4890-90b4-690afffb2b3d', 'created_at': datetime.datetime(2022, 1, 26, 19, 54, 52, 766133), 'updated_at': datetime.datetime(2022, 1, 26, 19, 56, 36, 394426), 'email': 'kidusmik@gmail.com'}"]
(hbnb)
(hbnb) help quit
Quit command to exit the program
(hbnb)
(hbnb) quit
kidusmik@ubuntu:~AirBnB_clone$
kidusmik@ubuntu:~AirBnB_clone$ cat file.json ; echo ""
{"Place.4e70b774-e1ce-45c6-8993-45e10ce48a46": {"id": "4e70b774-e1ce-45c6-8993-45e10ce48a46", "created_at": "2022-01-26T19:50:49.059166", "updated_at": "2022-01-26T19:50:49.059232", "__class__": "Place"}, "BaseModel.c37c1765-bd84-4890-90b4-690afffb2b3d": {"id": "c37c1765-bd84-4890-90b4-690afffb2b3d", "created_at": "2022-01-26T19:54:52.766133", "updated_at": "2022-01-26T19:56:36.394426", "email": "kidusmik@gmail.com", "__class__": "BaseModel"}}
kidusmik@ubuntu:~AirBnB_clone$
```
