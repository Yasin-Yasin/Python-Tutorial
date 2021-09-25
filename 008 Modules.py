# Python will execute whole file
# import my_module as mm

courses = ['History', 'Math', 'Physics', 'CompSci']

# index = mm.find_index(courses, 'Math') # We have to use module name to access function
# print(index)


# Despite importing only a function, it will execute whole module
# from my_module import * - It will everything from that module
from my_module import find_index, test

index = find_index(courses, 'Math')
print(index)

print(test)

# When we import modules python look for specific locations, we can see that directories 

import sys

print(sys.path)

# Add Directory to that list 
# sys.path.append('/home/Yasin/Desktop/My_Modules')


# Python Path Environment Variable - Another way to add directory in sys.path
# in Terminal - nano ~/,bash_profile
# add below line in .bash_profile file
# export PYTHONPATH="/home/Yasin/Desktop/My_Modules"  No space between = and path

# Standard Python Library

import random

random_course = random.choice(courses)
print(random_course)

import math

rads = math.radians(90)
print(rads)
print(math.sin(rads))

import datetime
import calendar

today = datetime.date.today()
print(today)

print(calendar.isleap(2020))

import os

print(os.getcwd())

# As these modules are python file themselves, we can see the location of these file by __file__
print(os.__file__)
print(datetime.__file__)