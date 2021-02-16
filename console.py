import cmd
import shlex
import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    
    prompt = '(hbnb) '
    
    def do_EOF(self, line):

        return True

    def do_quit(self, line):

        return True

    def do_create(self, classname):
        classname = shlex.split(classname)
        if classname == []: 
            print ("** class name missing **")
        else:
            models.storage.reload()
            objeto = eval(classname[0])()
            objeto.save()
            print (objeto.id)

    def do_show(self, classname):
        classname = shlex.split(classname)
        if  classname == []:
            print ("** class name missing **")
        else:
            for key, obj in models.storage.all().items():
                if obj.id == classname[1] and obj.__class__.__name__ == classname[0]:
                    print (obj.__str__)
                    return
            print ("** instance id missing **")


    def do_destroy(self, classname):
        pass

    def do_all(self, classname):
        pass

    def do_update(self, classname):
        pass


    """def do_prueba(self, args):
        args = shlex.split(args)
        print (args)
        #print (eval(args))
        print (type(args))
    """
if __name__ == "__main__":
    HBNBCommand().cmdloop()