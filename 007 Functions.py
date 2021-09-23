# pass 
# def hello_func():
#     pass

# Function Definition

def hello_func():
    print('Hello Function')

#  Calling a Function
hello_func()

# Keep Your code DRY

def hello():
    return 'Hello Function with return'

print(hello())

# Now  as we know our function return string we can apply string methods to it
print(hello().upper())

# Parameter

# def greeting_func(greeting):
#     return greeting

# Argument
# print(greeting_func('Good Morning'))

# Set Default value of parameter

def greeting_func(geeting, name = 'You'):
    return f'Welcome {name}'

print(greeting_func('Welcome'))

# args kwargs

def student_info(*args, **kwargs):
    print(args) # Tuple of Positional arguments
    print(kwargs) # Dictionary of Keyword Values

courses = ['Math', 'Art']
info = {'name' : 'John', 'age' : 24}

# student_info('Math', 'Art', name = 'John', age = 22)

# student_info(courses, info)

# To unpack course list as Positional argument and info Dictionary as keyword we have to add * ** in arguments otherwise it will take both as Positional argument
student_info(*courses, **info)  

# Keyword Arguments

# A keyword argument is an argument passed to a function or method which is preceded by a keyword and an equals sign. The general form is:

# function(keyword=value)

# Examples :

# Number of dyas per month, First value placeholder for indexing purpose, index 1 = Jan and So On
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]

def is_leap(year):
    """Return True for leap years, False for non-leap years.""" 

    return year%4 == 0 and (year % 100 != 0 or year % 400 == 0) 

def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29
    
    return month_days[month]


print(days_in_month(2020, 2))