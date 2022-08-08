
# AirBnB clone - The console

Is a command interpreter and the main purpose is to manage, manipulate and access the data in the backend through the console (command line tool ) very quickly and easily (like in shell project).

* We’ll manipulate data with JSON serialization/Deserialization (First DB engine).
* Manipulate Python packages
* Implement cmd module
* Implement uuid module
* args/kwargs
* datetime


## Install

git clone https://github.com/Ethiopian-boy/AirBnB_clone.git

```
cd AirBnB_clone
```
    
## CMD Commands




| Command |  Sample Usage     | Description                |
| :-------- | :------- | :------------------------- |
| Help | help |Show all available commands |
|Quit | quit | Exit to the prompt  |
|Create | create class | Create a new object |
| Show |show class name id| Retrieve an object from a file|
| All | all class | Display all objects in class |
| Update | update class id name key| Update objects and attributes|
|Destroy | destroy class| Destroy specified object|
|Count| class.count| Retrieve the number of instances of a class|



## Usage of command interpreter

# Interactive Mode:
1. Run program and show prompt with help command.
```
PROMPT~>AirBnB_clone# ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb) help quit
Quit command to exit the program

(hbnb)
(hbnb)
(hbnb) quit
PROMPT~>
```
# Usage Create:
 
With the create command, a new instance is created

```
(hbnb) create BaseModel
404edd71-8b1a-46a3-9c9a-5fb91feadce0
(hbnb)

```
# Usage All:

With the all command, all instances are displayed, returning a serialized json (string).

```
(hbnb) all BaseModel 404edd71-8b1a-46a3-9c9a-5fb91feadce0
[[BaseModel] (69afb018-e9e8-40cd-81af-23529caa9fcc) {'id': '69afb018-e9e8-40cd-81af-23529caa9fcc', 'created_at': datetime.datetime(2022, 8, 7, 13, 45, 0, 502667), 'updated_at': datetime.datetime(2022, 8, 7, 13, 45, 0, 502941)}, [BaseModel] (e87de47f-0be0-4118-91f2-e04c248df463) {'id': 'e87de47f-0be0-4118-91f2-e04c248df463', 'created_at': datetime.datetime(2022, 8, 7, 13, 45, 37, 485139), 'updated_at': datetime.datetime(2022, 8, 7, 13, 45, 37, 485164)}, [BaseModel] (404edd71-8b1a-46a3-9c9a-5fb91feadce0) {'id': '404edd71-8b1a-46a3-9c9a-5fb91feadce0', 'created_at': datetime.datetime(2022, 8, 8, 2, 54, 59, 25930), 'updated_at': datetime.datetime(2022, 8, 8, 2, 54, 59, 26492)}]
(hbnb)

```
# Usage Show:

With the show command, the instance is displayed, returning a dictionary of the id instance.

```
(hbnb) show BaseModel 404edd71-8b1a-46a3-9c9a-5fb91feadce0
[BaseModel] (404edd71-8b1a-46a3-9c9a-5fb91feadce0) {'id': '404edd71-8b1a-46a3-9c9a-5fb91feadce0', 'created_at': datetime.datetime(2022, 8, 8, 2, 54, 59, 25930), 'updated_at': datetime.datetime(2022, 8, 8, 2, 54, 59, 26492)}
(hbnb)

```
# Usage Update:

With the update command, the attributes of the instances are updated.
```
(hbnb) update BaseModel 404edd71-8b1a-46a3-9c9a-5fb91feadce0 first_name "Mulubrhan"
(hbnb) show BaseModel 404edd71-8b1a-46a3-9c9a-5fb91feadce0
[BaseModel] (404edd71-8b1a-46a3-9c9a-5fb91feadce0) {'id': '404edd71-8b1a-46a3-9c9a-5fb91feadce0', 'created_at': datetime.datetime(2022, 8, 8, 2, 54, 59, 25930), 'updated_at': datetime.datetime(2022, 8, 8, 2, 59, 45, 232383), 'first_name': 'Mulubrhan'}
(hbnb)
```

# Usage Count:

With the count command, count the number of instances.

```
(hbnb) BaseModel.count()
3
(hbnb)

```
# Usage Destroy:

With the Destroy command, instances are destroyed.
```
(hbnb) destroy BaseModel 404edd71-8b1a-46a3-9c9a-5fb91feadce0
(hbnb) show BaseModel 404edd71-8b1a-46a3-9c9a-5fb91feadce0
** no instance found **
(hbnb)
```


# non-interactive mode:

```
PROMPT~>AirBnB_clone# echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```
Mulubrhan Brhane 

Mfon Etuk
