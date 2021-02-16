#!/usr/bin/python3


""" Module console"""
import cmd
import shlex
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ class HBNBCommand """

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """ function do_EOF """

        return True

    def do_quit(self, line):
        """ function do_quit """

        return True

    def do_create(self, arg):
        """ function do_create """
        arg = shlex.split(arg)
        if arg == []:
            print("** class name missing **")
        else:
            models.storage.reload()
            objeto = eval(arg[0])()
            objeto.save()
            print(objeto.id)

    def do_show(self, arg):
        """ function do_show """
        arg = shlex.split(arg)
        if arg == []:
            print("** class name missing **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            for key, obj in models.storage.all().items():
                if obj.id == arg[1] and obj.__class__.__name__ == arg[0]:
                    print(obj.__str__())
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """ function do_destroy """
        arg = shlex.split(arg)
        if arg == []:
            print("** class name missing **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            el_obj = models.storage.all()
            for key, obj in el_obj.items():
                if obj.id == arg[1] and obj.__class__.__name__ == arg[0]:
                    del el_obj[key]
                    models.storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """ function do_all """
        arg = shlex.split(arg)
        if len(arg) == 0:
            models.storage.reload()
            la_lis = []
            for key, obj in models.storage.all().items():
                la_lis.append(obj.__str__())

            print(la_lis)

        else:
            models.storage.reload()
            la_lis = []
            for key, obj in models.storage.all().items():
                if obj.__class__.__name__ == arg[0]:
                    la_lis.append(obj.__str__())

            print(la_lis)

    def do_update(self, arg):
        """ function do_update """
        arg = shlex.split(arg)
        if arg == []:
            print("** class name missing **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            models.storage.reload()
            el_obj = models.storage.all()
            for key, obj in el_obj.items():
                if obj.id == arg[1] and obj.__class__.__name__ == arg[0]:
                    if len(arg) == 2:
                        print("** attribute name missing **")
                        return
                    elif len(arg) == 3:
                        print("** value missing **")
                        return
                    else:
                        nuevo_atr = arg[3]
                        if hasattr(obj, str(arg[2])):
                            nuevo_atr = (type(getattr(obj, arg[2])))(arg[3])
                        obj.__dict__[arg[2]] = nuevo_atr
                        models.storage.save()
                        return
            print("** no instance found **")

    """def do_prueba(self, args):
        args = shlex.split(args)
        print (args)
        #print (eval(args))
        print (type(args))
    """


if __name__ == "__main__":
    HBNBCommand().cmdloop()
