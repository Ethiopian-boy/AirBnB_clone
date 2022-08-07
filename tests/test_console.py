#!/usr/bin/python3
"""
Unittest for console command interpreter
"""
import unittest
from unittest.mock import patch
from io import StringIO
import pep8
import os
import json
import console
import tests
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):

    """Unittest for command interpreter"""
    @classmethod
    def setUpClass(self):
        """Set up test"""
        self.typing = console.HBNBCommand()

    @classmethod
    def tearDownClass(self):
        """Remove temporary file (file.json) created as a result"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8_console(self):
        """Pep8 console.py"""
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        file = (["console.py"])
        errors += style.check_files(file).total_errors
        self.assertEqual(errors, 0, 'Kindly fix Pep8')

    def test_pep8_test_console(self):
        """Pep8 test_console.py"""
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        file = (["tests/test_console.py"])
        errors += style.check_files(file).total_errors
        self.assertEqual(errors, 0, 'Kindly fix Pep8')

    def test_docstrings_in_console(self):
        """Test docstrings exist in console.py"""
        self.assertTrue(len(console.__doc__) >= 1)

    def test_docstrings_in_test_console(self):
        """Test docstrings exist in test_console.py"""
        self.assertTrue(len(self.__doc__) >= 1)

    def test_emptyline(self):
        """Test no user input"""
        with patch('sys.stdout', new=StringIO()) as dummy_output:
            self.typing.onecmd("\n")
            self.assertEqual(dummy_output.getvalue(), '')

    def test_quit(self):
        ''' Test quit'''
        with patch('sys.stdout', new=StringIO()) as dummy_output:
            self.typing.onecmd("quit")
            self.assertEqual('', dummy_output.getvalue())

    def test_EOF(self):
        ''' Test EOF'''
        with patch('sys.stdout', new=StringIO()) as dummy_output:
            self.typing.onecmd("EOF")
            self.assertEqual('\n', dummy_output.getvalue())

    def test_create(self):
        """Test cmd output: create"""
        with patch('sys.stdout', new=StringIO()) as dummy_output:
            self.typing.onecmd("create")
            self.assertEqual("** class name missing **\n",
                             dummy_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as dummy_output:
            self.typing.onecmd("User.all()")
            self.assertEqual("[]\n",
                             dummy_output.getvalue()[:7])
        with patch('sys.stdout', new=StringIO()) as dummy_output:
            self.typing.onecmd("create SomeClass")
            self.assertEqual("** class doesn't exist **\n",
                             dummy_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as dummy_output:
            self.typing.onecmd("create User")  # not used
            self.typing.onecmd("create User")  # just need to create instances

    def test_all(self):
        """Test cmd output: all"""
        with patch('sys.stdout', new=StringIO()) as dummy_output:
            self.typing.onecmd("all NonExistantModel")
            self.assertEqual("** class doesn't exist **\n",
                             dummy_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as dummy_output:
            self.typing.onecmd("all Place")
            self.assertEqual("[]\n", dummy_output.getvalue())

    def test_class_cmd(self):
        """Test cmd output: <class>.<cmd>"""
        with patch('sys.stdout', new=StringIO()) as dummy_output:
            self.typing.onecmd("User.count()")
            self.assertEqual(int, type(eval(dummy_output.getvalue())))

    def test_destroy(self):
        """Test cmd output: destroy"""
        with patch('sys.stdout', new=StringIO()) as dummy_output:
            self.typing.onecmd("destroy")
            self.assertEqual("** class name missing **\n",
                             dummy_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as dummy_output:
            self.typing.onecmd("destroy TheWorld")
            self.assertEqual("** class doesn't exist **\n",
                             dummy_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as dummy_output:
            self.typing.onecmd("destroy User")
            self.assertEqual("** instance id missing **\n",
                             dummy_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as dummy_output:
            self.typing.onecmd("destroy BaseModel 12345")
            self.assertEqual("** no instance found **\n",
                             dummy_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as dummy_output:
            self.typing.onecmd("City.destroy('123')")
            self.assertEqual("** no instance found **\n",
                             dummy_output.getvalue())

    def test_update(self):
        """Test cmd output: update"""
        with patch('sys.stdout', new=StringIO()) as dummy_output:
            self.typing.onecmd("update")
            self.assertEqual("** class name missing **\n",
                             dummy_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as dummy_output:
            self.typing.onecmd("update You")
            self.assertEqual("** class doesn't exist **\n",
                             dummy_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as dummy_output:
            self.typing.onecmd("update User")
            self.assertEqual("** instance id missing **\n",
                             dummy_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as dummy_output:
            self.typing.onecmd("update User 12345")
            self.assertEqual("** no instance found **\n",
                             dummy_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as dummy_output:
            self.typing.onecmd("update User 12345")
            self.assertEqual("** no instance found **\n",
                             dummy_output.getvalue())

    def test_show(self):
        """Test cmd output: show"""
        with patch('sys.stdout', new=StringIO()) as dummy_output:
            self.typing.onecmd("show")
            self.assertEqual("** class name missing **\n",
                             dummy_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as dummy_output:
            self.typing.onecmd("SomeClass.show()")
            self.assertEqual("** class doesn't exist **\n",
                             dummy_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as dummy_output:
            self.typing.onecmd("show Review")
            self.assertEqual("** instance id missing **\n",
                             dummy_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as dummy_output:
            self.typing.onecmd("User.show('123')")
            self.assertEqual("** no instance found **\n",
                             dummy_output.getvalue())


if __name__ == "__main__":
    unittest.main()