#!/usr/bin/python3
"""
The ``test_console`` module
==============================
Using ``test_console``
-------------------------
This is a test_console unittest file to test the console module.
"""
import unittest
from unittest.mock import patch
from io import StringIO
import os
from console import HBNBCommand
from models import storage

class TestConsole(unittest.TestCase):
    """Defines a class TestConsole.
    Test functionality of the console module.
    """
    help_quit = "Quit command to exit the program"
    help_EOF = "Exits the program"
    help_create = "Creates a new instance of a class, saves it to file\
 and prints the id"
    help_show = "Prints the string representation of an instance based on the\
 class name and id"
    help_destroy = "Deletes an instance based on the class name and id and save the\
 change into the JSON file"
    help_all = "Prints all string representation of all instances based or\
 not on the class name."
    help_update = "Updates an instance based on the class name and id by adding or\
 updating attribute and save the change into the JSON file"
    help_count = "Counts the number of instances of a certain class"

    all_classes_name = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def tearDown(self):
        """Remove storage file after test ends."""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_help_quit(self):
        """Tests if help message is as expected."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(f.getvalue().strip(), TestConsole.help_quit)

    def test_help_EOF(self):
        """Tests if help message is as expected."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual(f.getvalue().strip(), TestConsole.help_EOF)

    def test_help_create(self):
        """Tests if help message is as expected."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertEqual(f.getvalue().strip(), TestConsole.help_create)

    def test_help_show(self):
        """Tests if help message is as expected."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertEqual(f.getvalue().strip(), TestConsole.help_show)

    def test_help_destroy(self):
        """Tests if help message is as expected."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            self.assertEqual(f.getvalue().strip(), TestConsole.help_destroy)

    def test_help_all(self):
        """Tests if help message is as expected."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            self.assertEqual(f.getvalue().strip(), TestConsole.help_all)

    def test_help_update(self):
        """Tests if help message is as expected."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            self.assertEqual(f.getvalue().strip(), TestConsole.help_update)

    def test_help_count(self):
        """Tests if help message is as expected."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help count")
            self.assertEqual(f.getvalue().strip(), TestConsole.help_count)

    def test_create(self):
        """Tests if help message is as expected."""
        with patch('sys.stdout', new=StringIO()) as f:
            for i in TestConsole.all_classes_name:
                f.truncate(0)
                f.seek(0)
                HBNBCommand().onecmd("create" + " " + i)
                id_val = f.getvalue().strip()
                self.assertTrue(i + "." + id_val in storage._FileStorage__objects.keys())

    def test_alt_create(self):
        """Tests if help message is as expected."""
        with patch('sys.stdout', new=StringIO()) as f:
            for i in TestConsole.all_classes_name:
                f.truncate(0)
                f.seek(0)
                HBNBCommand().onecmd(i + ".create()")
                id_val = f.getvalue().strip()
                self.assertTrue(i + "." + id_val in storage._FileStorage__objects.keys())
