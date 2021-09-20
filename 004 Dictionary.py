from sys import stderr


student = {'name' : 'Safwan', 'age' : 25, 'courses' : ['Math', 'CompSci']}

print(student['name'])
print(student['courses']) # If Key doesn't exist it will give KeyError


# get method to access value
print(student.get('name'))
print(student.get('phone')) # It will return None instead of KeyError 
print(student.get('phone', 'Not Found')) # You can also change default value None

student['phone'] = '555-55555' # Adding Key-Value to dictionary
student['name'] = 'Sahil' # It will update as key already exist
print(student.get('phone', 'Not Found'))
print(student)

# update method
student.update({'name' : 'Sahil', "age" : 30, 'phone' : '555- 55565'})
print(student)

# Delete key-value pair

# del student['age']
# print(student)

# pop() method

age = student.pop('age') # It will value of deleted Key
print(age)
print(student)

# Len()
print(len(student))

# print keys
print(student.keys()) 

# print values
print(student.values()) 

# items method
print(student.items())

# loop on dictionary

# It will print all keys
for key in student:
    print(key)
# It will print Values
for key in student:
    print(student[key])

# Key and value both
for key, value in student.items():
    print(key, value)