'''
# LISTS
#Lists in python are equivalent to structures such as dynamic vectors in programming languages such as C, C++
#List is a mutable data structure which allows the list content can be modified after it has been created
'''

'''
# TUPLES
# `tuple` class in python is a data structure that can store elements of different types
# Tuples are immutable, the content cannot be modified after is has been created
'''

# Python Classes

class Protocol(object):
    def __init__(self, name, number, description):
        self.name = name
        self.number = number
        self.description = description
    
    def getProtocolInfo(self):
        return f"{self.name} {str(self.number)} {self.description}"


class BaseClass:
    def __init__(self, property) -> None:
        self.property = property
    
    def message(self):
        print("Hi MOM")
    
    def message_base_class(self):
        print("Hello MOM")
    
class ChildClass(BaseClass):
    def __init__(self, property) -> None:
        super().__init__(property)
    
    def message(self):
        print("Child class")
        print("Inherited from base class")


if __name__ == '__main__':
    base_obj = BaseClass('property')
    base_obj.message()
    child_obj = ChildClass('property')
    child_obj.message()
    child_obj.message_base_class()

'''
Two built-in functions, `isinstance()` and `issubclass()` are used to check inheritances.
One of these methods that we use to check if a class is a subclass of another is through the `issubclass()` method. 
'''

print(issubclass(ChildClass, BaseClass)) # True
print(issubclass(BaseClass, ChildClass)) # False


'''
`isinstance() method allows you to check if an object is an instance of a class.
This method returns true if the object is the instance of the class that is passed as the second parameter
'''

print(isinstance(base_obj, BaseClass)) # True
print(isinstance(child_obj, ChildClass)) # True
print(isinstance(child_obj, BaseClass)) # True


class MainClass:
    def msg_main(self):
        print('main class')

class MainClass2:
    def msg2(self):
        print('Main class 2')

class ChildClass(MainClass, MainClass2):
    def msg_child(self):
        print('child')
        print('inherited from mainclass and mainclass2')

if __name__ == '__main__':
    child_obj = ChildClass()
    child_obj.msg_main()
    child_obj.msg2()
    child_obj.msg_child()


'''
Multi level inheritance
'''

class MainClass:
    def message_main(self):
        print('Welcome to Main Class')
class Child(MainClass):
    def message_child(self):
        print('Welcome to Child Class')
        print('This is inherited from Main')
class ChildDerived(Child):
    def message_derived(self):
        print('Welcome to Derived Class')
        print('This is inherited from Child')

if __name__ == '__main__':
    child_derived_obj = ChildDerived()
    child_derived_obj.message_main()
    child_derived_obj.message_child()
    child_derived_obj.message_derived()
    print(issubclass(ChildDerived, Child))
    print(issubclass(ChildDerived, MainClass))
    print(issubclass(Child, MainClass))
    print(issubclass(MainClass, ChildDerived))
    print(isinstance(child_derived_obj, Child))
    print(isinstance(child_derived_obj, MainClass))
    print(isinstance(child_derived_obj, ChildDerived))


##### FILES ###############
f = open('file', 'w')
type(f) #<class '_io.TextIOWrapper'>
f.close()

file_descriptor = open("read_file_properties.py", "r+") 
print("Content: "+file_descriptor.read())
print("Name: "+file_descriptor.name)
print("Mode: "+file_descriptor.mode)
print("Encoding: "+str(file_descriptor.encoding))
file_descriptor.close()

allLines = file_descriptor.readlines() #read all the lines of the file

#read line by line
with open('file', 'r') as file:
    for line in file:
        print(line)


#### TRY and EXCEPT blocks
'''
all the built-in python exceptions form a hierarchy of classes. The following script dumps all predefined exception classes in the form of a tree like printout
'''
def printExceptionsTree(ExceptionClass, level = 0):
    if level > 1:
        print("   |" * (level - 1), end="")
    if level > 0:
        print("   +---", end="")
    print(ExceptionClass.__name__)
    for subclass in ExceptionClass.__subclasses__():
        printExceptionsTree(subclass, level+1)
printExceptionsTree(BaseException)


### Modules and Packages

# when a module is imported, its content is implicitly executed by python. 
# we can get more information about methods and other entities from a specific modules using the `dir()` method
# this method returns a list with all the definitions (variables, functions, classes) contained in a module


# a package is simply a directory that contains other packages and modules. Also in python, for a directory to be considered a package, it must include a module called `__init__.py`
# in most cases, this file will be empty, however it can be used to initialize package-related code


#### Managing parameters in Python
import argparse
class Parameters:
    def __init__(self, **kwargs) -> None:
        self.param1 = kwargs.get('param1')
        self.param2 = kwargs.get('param2')

def view_params(input_params):
    print(input_params.param1)
    print(input_params.param2)
parser = argparse.ArgumentParser(description='Testing arguments')
parser.add_argument('-p1', dest='param1', help='parameter 1')
parser.add_argument('-p2', dest='param2', help='parameter 2')
params = parser.parse_args()
input_params = Parameters(param1=params.param1, param2=params.param2)
view_params(input_params)


import argparse
if __name__ == "__main__":
    description = """ Uses cases:
        +  Basic scan:
            -target 127.0.0.1
        + Specific port:
            -target 127.0.0.1 -port 21
        + Port list:
            -target 127.0.0.1 -port 21,22
        + Only show open ports
            -target 127.0.0.1 --open True """
    parser = argparse.ArgumentParser(description='Port scanning', epilog=description,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-target", metavar='TARGET', dest="target", help="target to scan",required=True)
    parser.add_argument("-ports", dest="ports", help="Please, specify the target port(s) separated by comma[80,8080 by default]", default = "80,8080")
    parser.add_argument('-v', dest='verbosity', default=0, action="count", help="verbosity level: -v, -vv, -vvv.")
    parser.add_argument("--open", dest="only_open", action="store_true", help="only display open ports", default=False)


from optparse import OptionParser
class Parameters:
    """Global parameters"""
    def __init__(self, **kwargs):
        self.param1 = kwargs.get("param1")
        self.param2 = kwargs.get("param2")
 
def view_parameters(input_parameters):
    print(input_parameters.param1)
    print(input_parameters.param2)
parser = OptionParser()
parser.add_option("--p1", dest="param1", help="parameter1")
parser.add_option("--p2", dest="param2", help="parameter2")
(options, args) = parser.parse_args()
input_parameters = Parameters(param1=options.param1,param2=options.param2)
view_parameters(input_parameters)


## Virtual Environments, Managing Dependencies

'''
we also have the ability to create the `requirements.txt` file from the project source code.
for this task, we can use `pipreqs` module,
pipreqs <projectPath>
'''

'''
`virtualenv` is a python module that enables you to build isolated, virtual environments. Essentially, you must create a folder that contains all the executable files and modules.
'''

'''
pip install virtualenv
cd <project>
virtualenv <virtualEnvName>
source bin/activate
'''

