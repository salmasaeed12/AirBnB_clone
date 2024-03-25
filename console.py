#!/usr/bin/env python3
"""
Entry point for the command interpreter.
"""

import cmd
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the AirBnB clone.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program on EOF (Ctrl-D).
        """
        print()  # Print a newline before exiting
        return True

    def emptyline(self):
        """
        Do nothing on an empty line.
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of User,
          saves it to the JSON file, and prints its id
        Usage: create User
        """
        if not arg:
            print("** class name missing **")
            return
        new_user = User()
        new_user.save()
        print(new_user.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
          based on the class name and id
        Usage: show User <id>
        """
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = "User." + args[1]
        if obj_key in storage.all():
            print(storage.all()[obj_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class
          name and id (save the change into the JSON file)
        Usage: destroy User <id>
        """
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = "User." + args[1]
        if obj_key in storage.all():
            del storage.all()[obj_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_update(self, arg):
        """
        Updates an instance
          based on the class name and id by
            adding or updating attribute (save the change into the JSON file)
        Usage: update User <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if len(args) < 4:
            print("** instance id missing **")
            return
        obj_key = "User." + args[1]
        if obj_key in storage.all():
            obj = storage.all()[obj_key]
            setattr(obj, args[2], args[3].strip('"'))
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all instances
          of the given class, or all
            instances of all classes if no class name is provided.
        """
        if arg:
            # Print all instances of the given class
            for obj in storage.all().values():
                if type(obj).__name__ == arg:
                    print([str(obj)])
        else:
            # Print all instances of all classes
            for obj in storage.all().values():
                print([str(obj)])

    def default(self, arg):
        """Called on an input line when the command prefix is not recognized"""
        args = arg.split(".")
        if len(args) < 2:
            print("*** Unknown syntax:", arg)
            return
        classes = ["User", "State", "City", "Amenity", "Place", "Review"]
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if args[1] == "all()":
            self.do_all(args[0])
        elif args[1] == "count()":
            print(len([v for k, v in storage.all().items()
                       if v.__class__.__name__ == args[0]]))
        elif args[1].startswith("show("):
            self.do_show(args[0] + " " + args[1][5:-2])
        elif args[1].startswith("destroy("):
            self.do_destroy(args[0] + " " + args[1][8:-2])
        elif args[1].startswith("update("):
            self.do_update(args[0] + " " + args[1][7:-1])
        else:
            print("*** Unknown syntax:", arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
