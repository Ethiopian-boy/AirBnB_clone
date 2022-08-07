#!/usr/bin/python3
"""
This is the entry to command interpreter
"""
import cmd
import ast
import json
from models.base_model import BaseModel
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    Entry to command interpreter
    """

    prompt = "(hbnb) "  # this is a public instance variable from cmd
    classes = {"Amenity", "BaseModel", "City", "Place",
               "Review", "State", "User"}

    def do_EOF(self, line):
        """Exits after receiving the EOF signal"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Overwrite default behavious to repeat it last cmd"""
        pass

    def do_create(self, line):
        """Creates a new instance of class specified by the user
        and prints its id
        """
        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            instance = eval(line)()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance based
        on the class name and id
        """
        new_storage = storage.all()
        response = validateInstance(line, new_storage)

        if (((isinstance(response[0], bool)) and response[0] is False) and
           isinstance(response[1], str)):
            print(response[1])  # this would mean error
            return
        else:
            value = new_storage[response[1]]  # this would be the name
            print(value)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        new_storage = storage.all()
        response = validateInstance(line, new_storage)

        if (((isinstance(response[0], bool)) and response[0] is False) and
           isinstance(response[1], str)):
            print(response[1])  # this would mean error
            return
        else:
            del new_storage[response[1]]  # del the instance from storage
            storage.save()

    def do_all(self, line):
        """This prints all string representation of all instances
        based or not on the class name i.e Print all objects
        or all objects of specified class
        """
        args = parse(line)
        obj_list = []
        if len(line) == 0:
            for objs in storage.all().values():
                obj_list.append(objs)
            print(obj_list)
        elif args[0] in HBNBCommand.classes:
            for key, objs in storage.all().items():
                if args[0] in key:
                    obj_list.append(objs)
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        """
        new_storage = storage.all()
        args = parse(line)
        if len(args) >= 4:
            key = "{}.{}".format(args[0], args[1])
            attr_cast = type(eval(args[3]))
            arg3 = args[3]
            arg3 = arg3.strip('"')
            arg3 = arg3.strip("'")
            try:
                setattr(new_storage[key], args[2], attr_cast(arg3))
            except KeyError:
                print("** no instance found **")
                return
            new_storage[key].save()
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in new_storage.keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        else:
            print("** value missing **")
        new_storage = {}

    def do_count(self, line):
        """Display the count of instances of a class"""
        if line in HBNBCommand.classes:
            count = 0
            for key, objs in storage.all().items():
                if line in key:
                    count += 1
            print(count)
        else:
            print("** class doesn't exist **")

    def default(self, line):
        """Accepts class name alongside a method
        e.g <class name>.all()
        """
        method_call_name = None
        method_args = None
        functions = {"all": self.do_all, "update": self.do_update,
                     "show": self.do_show, "count": self.do_count,
                     "destroy": self.do_destroy, "update": self.do_update}
        args = line.split('.')
        class_arg = args[0]
        if len(args) == 1:
            print("*** Unknown syntax: {}".format(line))
            return
        try:
            args = args[1].split('(')
            command = args[0]
            if command == 'all':
                method_call_name = command
                method_args = class_arg
            elif command == 'count':
                method_call_name = command
                method_args = class_arg
            elif command == 'show':
                args = args[1].split(')')
                id_arg = args[0]
                id_arg = id_arg.strip("'")
                id_arg = id_arg.strip('"')
                arg = class_arg + ' ' + id_arg
                method_call_name = command
                method_args = arg
            elif command == 'destroy':
                args = args[1].split(')')
                id_arg = args[0]
                id_arg = id_arg.strip('"')
                id_arg = id_arg.strip("'")
                arg = class_arg + ' ' + id_arg
                method_call_name = command
                method_args = arg
            elif command == 'update':
                # sampe: "38f22813-2753-4d42-b37c-57a17f1e4f88",
                # {'first_name': "John", "age": 89}
                args = args[1].split(',')
                # item 1 would be the id
                id_arg = args[0].strip("'")
                id_arg = id_arg.strip('"')
                # while d rest is d other
                # args({'first_name': "John", "age": 89})
                if args[1].lstrip(' ').startswith('{'):
                    attr_dict = str(args[1]) + ',' + str(args[2])
                    arg = attr_dict.rstrip(')')
                    # dictionary = dict(subString.split(":")
                    # for subString in arg.split(","))
                    method_args = class_arg + ' ' + id_arg + ' ' + str(arg)
                else:
                    attr_name = args[1].strip(',')
                    attr_val = args[2]
                    attr_name = attr_name.strip(' ')
                    attr_name = attr_name.strip("'")
                    attr_name = attr_name.strip('"')
                    attr_val = attr_val.strip(' ')
                    attr_val = attr_val.strip(')')
                    arg = class_arg + ' ' + id_arg + ' ' + attr_name \
                        + ' ' + attr_val
                    method_args = arg
                method_call_name = command
            else:
                print("*** Unknown syntax: {}".format(line))
            if method_call_name is not None:
                func = functions[method_call_name]
                func(method_args)
        except ValueError:
            print("*** Unknown syntax: {}".format(line))


def parse(line):
    """A helper method to parse user typed input
    on the cmd line
    """
    return tuple(line.split())


def validateInstance(line, obj_dict):
    """A helper method to validate users typed input on
    the cmd line
    """
    if len(line) == 0:
        return False, "** class name missing **"
    args = parse(line)
    if args[0] not in HBNBCommand.classes:
        return False, "** class doesn't exist **"
    try:
        if args[1]:
            name = "{}.{}".format(args[0], args[1])
            # since obj_dict was passed from models, it has been
            # reloaded already in the magic file __init__.py
            try:
                value = obj_dict[name]
                return True, name
            except KeyError:
                return False, "** no instance found **"
    except IndexError:
        return False, "** instance id missing **"


if __name__ == "__main__":
    HBNBCommand().cmdloop()
