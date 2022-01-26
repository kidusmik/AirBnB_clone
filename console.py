#!/usr/bin/python3
"""
This is the "console" file.

The console file contains the entry point of the command interpreter.
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Defines a class HBNBCommand.

    Attributes:
        prompt (str): prompt to display to the user
    """
    prompt = "(hbnb) "
    all_classes = {'BaseModel': BaseModel}

    def do_exit(self, arg):
        exit()

    def do_EOF(self, arg):
        print()
        exit()

    def help_exit(self):
        print('Quit command to exit the program')

    def emptyline(self):
        pass

    def do_create(self, arg):
        if len(arg.split()) < 1:
            print('** class name missing **')
        else:
            if arg in HBNBCommand.all_classes.keys():
                obj = HBNBCommand.all_classes[arg]()
                obj.save()
                print(obj.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, arg):
        args = arg.split()
        if len(args) < 1:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.all_classes.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print('** instance id missing **')
        else:
            key_obj = args[0] + "." + args[1] 
            try:
                print(storage._FileStorage__objects[key_obj])
            except KeyError:
                print('** no instance found **')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
