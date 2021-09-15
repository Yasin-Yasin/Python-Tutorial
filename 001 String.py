# STANDARD OUTPUT
print("Hello World")

# VARIABLE
message = "Hello World"
print(message)

# ESCAPE SEQUENCE
print('Salman\'s Pen')

# MULTILINE STRING
print("""I am Human
I live in Gujarat""")

# len() FUNCTION
print(len(message))

# STRING SLICING
print(message[10])
print(message[:5])
print(message[6:])

# STRING METHODS :
	
print(message.lower())
print(message.upper())
# Returns a number of occurence
print(message.count('l'))
#return index number 
print(message.find('World'))
# Returns a -1 if it can not find a word
print(message.find('Universe'))

# Returns a new string
new_message = message.replace('World', 'Universe')
print(new_message)

#Concatenating
greeting = 'Hello'
name = "Safwan"

#newMassage = greeting + name
newMassage = "{}, {}. Welcome".format(greeting,name)
nm = f"{greeting}, {name.upper()}."
print(newMassage)
print(nm)

# dir() and help()
print(dir(name))
print(help(str.find))