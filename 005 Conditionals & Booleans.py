# Comparisons
# Equal :               ==
# Not Equal :           !=
# Greater Than :        >
# Less Than :           <
# Greater or  Equal :   >=
# Less or  Equal :      <=
# Object  Identity :    is

# if block will be executed only if condition is true..
if True:
    print("Conditinal  was true")

if False:
    print("Conditinal  was False")

# else
language = 'Java'

if language == 'Python':
    print("Language is Python")
else:
    print('No Match')

# elseif -elif

if language == 'Python':
    print("Language is Python")
elif language == 'Java':
    print("Language is Java")
elif language == 'Javascript':
    print("Language is Javascript")
else:
    print('No Match')

# BOOLEAN - and or not

user = "Admin"
logged_in = True

if user == 'Admin' and logged_in:
    print("Admin Page")
else:
    print("Bad Creds")

# not
if not logged_in:
    print("Please Log In")
else:
    print("Welcome")

# is
a = [1,2,3]
b = [1,2,3]

print(a == b)

b = a # Now a is b will be true.

print(id(a))
print(id(b))

print(a is b) # Comparing identity : id(a) == id (b)
print(id(a) == id(b))

# False Values : Below Condition will be evaluated as False
    # False
    # None  - will be Flase
    # Zero of any numeric type
    # Any empty sequence, for example, "", (), []
    # Any empty mapping, for example, {}

condition = 'Test'

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")