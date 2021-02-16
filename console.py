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
        elif len(classname) == 1:
            print ("** instance id missing **")
        else:
            for key, obj in models.storage.all().items():
                if obj.id == classname[1] and obj.__class__.__name__ == classname[0]:
                    print (obj.__str__())
                    return
            print ("** no instance found **")


    def do_destroy(self, classname):
        classname = shlex.split(classname)
        if  classname == []:
            print ("** class name missing **")
        elif len(classname) == 1:
            print ("** instance id missing **")
        else:
            el_obj = models.storage.all()
            for key, obj in el_obj.items():
                if obj.id == classname[1] and obj.__class__.__name__ == classname[0]:
                    del(el_obj[key])
                    models.storage.save()
                    return
            print ("** no instance found **")

    def do_all(self, classname):
        classname = shlex.split(classname)
        if  len(classname) == 0:
            models.storage.reload()
            la_lis = []
            for key, obj in models.storage.all().items():
                la_lis.append(obj.__str__())
                    
            print(la_lis)

        else:
            models.storage.reload()
            la_lis = []
            for key, obj in models.storage.all().items():
                if obj.__class__.__name__ == classname[0]:
                    la_lis.append(obj.__str__())
                    
            print (la_lis)

    def do_update(self, classname):
        classname = shlex.split(classname)
        if  classname == []:
            print ("** class name missing **")
        elif len(classname) == 1:
            print ("** instance id missing **")
        else:
            models.storage.reload()
            el_obj = models.storage.all()
            for key, obj in el_obj.items():
                    if obj.id == classname[1] and obj.__class__.__name__ == classname[0]:
                        if len(classname) == 2:
                            print("** attribute name missing **")
                            return
                        elif len(classname) == 3:
                            print("** value missing **")
                            return
                        else:
                            nuevo_atr = classname[3]
                            if hasattr(obj, str(classname[2])):
                                nuevo_atr = (type(getattr(obj, classname[2])))(classname[3])
                            obj.__dict__[classname[2]] = nuevo_atr
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