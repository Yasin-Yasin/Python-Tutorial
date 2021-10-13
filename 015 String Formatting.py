person = {'name' : 'John', 'age' : 23}

# Without any Formatting
sentence = "My name is " + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
print(sentence)

# ----------------------------------- format() METHOD ----------------------------------------

sentence1 = "My name is {} and I am {} years old.".format(person['name'], person['age'])
print('Format Method : ', sentence1)

tag = 'h1'
text = 'This is a headline'

# Use number for placeholder - useful when using variable multiple time in string
sentence2 = '<{0}>{1}</{0}>'.format(tag,text)
print(sentence2)

# Dictionary
sentence3 = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
print(sentence3)

# List
l = ["salman", 25]
sentence4 = 'My name is {0[0]} and I am {0[1]} years old.'.format(l)
print(sentence4)

# Attribute
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Jack', '33')

sentence5 = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(sentence5)

# Keyword argument
sentence6 = 'My name is {Name} and I am {Age} years old.'.format(Name = 'Sahil', Age = 20)
print(sentence6)

# Unpacking Dictionary
person1 = {'name' : 'Jenn', 'age' : 33}
sentence7 = 'My name is {name} and I am {age} years old.'.format(**person1)
print(sentence7)

# Advance formatting :

# Add 0 before number
for i in range(1, 11):
    sentence8 = 'The value is {:02}'.format(i) # 0 - add 0 , 2 - 2 digit
    print(sentence8)

# 2 Decimal places
pi = 3.14159265

sentence9 = 'Pi is equal to {:.2f}'.format(pi)
print(sentence9)

# Comma seperator for large number
sentence10 = "1 MB is equal to {:,} bytes".format(1000**2)
sentence10 = "1 MB is equal to {:,.2f} bytes".format(1000**2) # Combination of comma and 2 decimal point
print(sentence10)

# Date
import datetime

my_date = datetime.datetime(2021, 10, 7, 12, 28, 9)

print(my_date)

# October 07, 2021
my_date1 = '{:%B %d, %Y}'.format(my_date)
print(my_date1)

# October 07, 2021 fell on thirsday and was 280th day of the year
my_date2 = '{0:%B %d, %Y} fell on {0:%A} and is the {0:%j}th day of the year.'.format(my_date) # 0 for placeholder 0 = my_date) 
print(my_date2)