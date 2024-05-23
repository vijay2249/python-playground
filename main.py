print("Hi MOM!!!")

msg = "I want to meet Harry Styles"
print(msg)

msg = "I want to see One Direction reunion"
print(msg)

name = "liam payne"
print(name.title()) # Liam Payne
print(name.upper()) # LIAM PAYNE
print(name.lower()) # liam payne

band = "one Direction"
introduction = f"The biggest band on the planet, {band.title()}"
print(introduction)

print("Languages: \nTelugu\n\tEnglish\n\t\tSpanish")

whiteSpacesString = '    has_spaces    '
print(whiteSpacesString.lstrip()) # 'has_spaces    '
print(whiteSpacesString.rstrip()) # '    has_spaces' 
print(whiteSpacesString.strip()) # 'has_spaces'

url = 'https://coachbeardjr.vercel.app'
print(url.removeprefix('https://')) # 'coachbeardjr.vercel.app'

message = "One of Python's strengths is its diverse community."
print(message)

quote = 'Albert Einstein once said, “A person who never made a mistake never tried anything new.”'
print(quote)

# Integets - 2, 4, 222
# Floats - 0.22

universe_age = 14_000_000_000
print(universe_age) # 14000000000


a,b,c = 0,1,2 # multiple assignment

# Python doesnt have built-in constants

MAX_UNIT = 256 # Constants representation - variables in all caps


# -----------------------------------------
# -----------------------------------------
# -----------------------------------------

# LISTS
# A list is a collection of items in a particular order

bicycles = ['trek', 'cannondale', 'redline']
print(bicycles) # ['trek', 'cannondale', 'redline']
print(bicycles[0].title()) # Trek
print(bicycles[1]) # 'cannondale
print(bicycles[-1]) # 'redline'

names = ['Liam Payne', 'Nail Horan', 'Harry Styles', 'Louis Tomlinson', 'Zyan Malik']
for name in names:
    print(name)

bicycles[0] = 'Hardline'
bicycles.append('ducati')

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles) # ['ducati', 'honda', 'yamaha', 'suzuki']

del motorcycles[0]
print(motorcycles) # ['honda', 'yamaha', 'suzuki']
lost = motorcycles.pop()
print(lost) # 'suzuki'
print(motorcycles) # ['honda', 'yamaha']
first = motorcycles.pop(0)
print(first) # 'honda'
print(motorcycles) # ['yamaha']
motorcycles.remove('yamaha')
print(motorcycles) # []

# remove() method deletes only the first occurrence of the value you specify

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars) # ['audi', 'bmw', 'subaru', 'toyota']
cars.sort(reverse=True)
print(cars) # ['toyota', 'subaru', 'bmw', 'audi']

# sort() - modifies the original list
# sorted() return the new list with sorted values, and keeps the original list as it is

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars) # ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars) # ['subaru', 'toyota', 'audi', 'bmw']

print(len(cars)) #4


magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")

for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits) # 0
max(digits) # 9
sum(digits) # 45

squares = [values**2 for value in range(1,11)]
print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

complete_list = list(range(1,1_000_001))
min(complete_list)
max(complete_list)
sum(complete_list)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # ['charles', 'martina', 'michael']
print(players[1:4]) # ['martina', 'michael', 'florence']
# If you omit the first index in a slice, Python automatically starts your slice at the beginning of the list
print(players[2:]) # ['michael', 'florence', 'eli']
print(players[-3:]) # ['michael', 'florence', 'eli']
# You can include a third value in the brackets indicating a slice. If a third value is included, this tells Python how many items to skip between items in the specified range.

new_copy_list = players[:]

new_copy_list = players #this points to the same players object, so any actions done on new_list will affect the players object as well


# -----------------------------------------
# -----------------------------------------
# -----------------------------------------

# TUPLES
# an immutable list is called a tuple
dimensions = (200, 50)
print(dimensions[0]) # 200
print(dimensions[1]) # 50

my_t = (3,)

# Although you can’t modify a tuple, you can assign a new value to a variable that represents a tuple.



# -----------------------------------------
# -----------------------------------------
# -----------------------------------------

# if-elif-else conditions
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings) # True
print('pepperoni' in requested_toppings) # False


banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")



# -----------------------------------------
# -----------------------------------------
# -----------------------------------------

# DICTIONARIES

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color']) # 'green'
print(alien_0['points']) # 5

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0) # {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
alien_0['color'] = 'yellow'
print(alien_0['color']) # 'yellow'

del alien_0['points']
print(alien_0) # { 'color': 'yellow', 'x_position':0, 'y_position': 25}

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
print(favorite_languages)

print(alien_0.get('points', "No point value assigned..")) # get the value of 'points' key, if such key wont exists then return this default value

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

user_0.keys() # returns keys in dictionary
user_0.values() # returns values of dictonary keys



# -----------------------------------------
# -----------------------------------------
# -----------------------------------------

# USER INPUT and WHILE LOOPS


# break, continue and using flags in while/for loops


# -----------------------------------------
# -----------------------------------------
# -----------------------------------------

# FUNCTIONS

# The docstrings are used to describe what the function does., when python generates documentation for the functions in the program, it looks for a string immediately after the functions definition.

def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('Harry')

# for function 'greet_user'
# Arguments -> "Harry" -> piece of information thats passed from a function call to a function
# Parameters -> username -> piece of information the function needs to do its job

'''
You can pass arguments to your functions in a number of ways
1. Positional Arguments - which need to be in the same order the parameters are written
2. Keyword arguments - where each argument consists of a variable name and a value and lists and dictionaries of values


When you call a function, Python must match each argument in the function call with a parameter in the function definition. The simplest way to do this is based on the order of the arguments provided.
Values matched up this way are called _positional arguments_
'''

def great_man_once_said(who, what):
    said = f"{who}: {what}!"
    print(said)

great_man_once_said("harry styles", "3 banana's for a euro")
great_man_once_said("Daniel", "Pieeeerrrreeeee Gaslyyyyyyyyyyyyyy")

''' Order matters in positional Arguments '''

'''
Keyword argument is a name-value pair that you pass to a function. You directly associate the name and the value within the argument so when you pass the argument to the function, theres no confusion.
'''
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')


# Default parameter values
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')

# When you use default values, any parameter with a default value needs to be listed after all the parameters that dont have default values.
# This allows Python to continue interpreting positional arguments correctly


# A function doesnt always have to display its output directly. Instead, it can process some data and then return a value or set of values.
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('Coach', 'Beard Jr')
print(musician)

# function can return any data type and any number of values from a function

# When you pass a list to a function, the function can modify the list. Any changes made to the list inside the functions body are permanent, allowing you to work effectively even when you are dealing with large amounts of data
# to keep the original list same, pass the copied list argument to the function using the slice notation

# Arbitary Number of Arguments
def band_members(*args):
    for member in args:
        print(member)

band_members('Liam Payne', "Harry Styles", "Zayn Malik", "Nail Horan", "Louis Tomlinson")

def band_and_its_members(**kwargs):
    print(kwargs['band'])
    for member in kwargs['members']:
        print(f"\t{member}")

band_and_its_members(band='One Direction', members=['Liam', 'Nail','Louis','Zyan','Harry'] )

# Storing functions in modules

# 'import' statment tells python to make the code in a module available in the currently running program file

import time #import complete module
from random import random #import specific function
from date import date as da #alias for a function, same can be done for module as well
from requests import * #import every thing from module


# -----------------------------------------
# -----------------------------------------
# -----------------------------------------

# CLASSES

'''
When you write a class, you define the general behavior that a whole category of objects can have
'''

'''
When you create individual objects from the class, each object is automatically equipped with the general behavior

Making an object from a class is called _instantiation_, and you work with _instances_ of class.
'''

class Dog: #by convention, capitalized names refer to classes in Python
    ''' Classes learning '''

    def __init__(self, name, age): #runs automatically whenever we create a new instance of the class
        # the 'self' parameter is required in the method definition, and it must come first, before the other parameters.
        # it must be included in the definition because when python calls this method later, the method call will automatically pass the 'self' argument
        # Every method call associated with an instance automatically passes 'self', which is a reference to the instance itself, it gives the individual instance access to the attributes and methods in the class.
        ''' Initialize the data in class '''
        self.name = name
        self.age = age
    
    def sit(self):
        ''' random method '''
        print(f"{self.name} is now sitting")
    
    def roll_over(self):
        ''' another method '''
        print(f"{self.name} rolled over!")

''' 
Method having two leading underscores and two trailing underscores, a convention that helps prevent python's default method names from conflicting with your method names 
Any variable prefixed with 'self' is available to every method in the class and can also be able to access these variables through any instance created from the class.

Variables that are accessible through instances like this are called _attributes_
'''

my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

''' 
You can makke as many instances from one class as you need, as long as you give each instance a unique variable name or it occupies a unique spot in a list or dictionary
'''

# Setting default value for an attribute


# Inheritance
'''
When one class inherits from another, it takes on the attributes and methods of the first class
The original class is called the _parent class_ and the new class is called _child class_. 
The child class can inherit any or all of the attributes and methods of its parent class, but its also free to define new attributes and methods of its own.
'''

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        
        print(f"Range {range} miles on full charge")

class ElectricCar(Car): # name of the parent must be included in parenthesis in the definition of a child class
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        # super() function is a special function that allows you to call a method from the parent class. 
        # self.battery_size = 40
        self.battery_size = Battery()
    
    # def describe_battery(self):
        # print(f"{self.battery_size}-KWh battery")

    '''
    to override any parent method, you define a method in the child class with the same name as the method you want to override in the parent class
    '''
    def fill_gas_tank(self):
        print("This car doesnt have a gas tank!")




my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
# my_leaf.describe_battery()
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()


# we can include a module level docstring that briefly describes the contents of the module



# -----------------------------------------
# -----------------------------------------
# -----------------------------------------

# FILES and EXCEPTIONS

# Reading from a FILE
'''
When you want to work with the information in a text file, the first step is to read the file into memory.
'''

from pathlib import Path

path = Path('fileName.extension') #exact location 
contents = path.read_text()
print(contents)


# Handing Exceptions

try:
    print()
except Exception as error:
    print(error)
else:
    print("else block")
finally:
    print("finally")


# JSON

from pathlib import Path
import json

numbers = [2,3,5,7,11]
path = Path('numbers.json')
contents = json.dumps(numbers) #function to generate a string containing the JSON representation of the data we are working with
path.write_text(contents)

new_contents = path.read_text()
num = json.loads(new_contents) #function takes the JSON formatted string and returns a python object to work with
