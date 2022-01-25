#!/usr/bin/python3
"""
This is the "console" file.

The console file contains the entry point of the command interpreter.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines a class HBNBCommand.

    Attributes:
        prompt (str): prompt to display to the user
    """
    prompt = "(hbnb) "

    def do_exit(self, arg):
        exit()

    def do_EOF(self, arg):
        print()
        exit()

    def help_exit(self):
        print('Quit command to exit the program')

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
