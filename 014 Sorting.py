# List

li = [9,1,8,2,7,3,6,4,5]
s_li = sorted(li)   

print("Sorted List\t", s_li) # This function doesn't change original list, It returns new sorted list
print('Original List\t', li)

li.sort() # sort method sort original list, doesn't return new list, this method is specific to List obj
print('Original List, Now Sorted\t', li) 

# Reverse Sorting 
li1 = [9,1,8,2,7,3,6,4,5]
s_li1 = sorted(li1, reverse=True)

li1.sort(reverse=True)

print("Sorted Reverse List\t", s_li1)
print("Sorted Reverse Original List\t", li1)

# Tuple
tup = (9,1,8,2,7,3,6,4,5)

s_tup = sorted(tup)

print('Sorted Tuple\t', s_tup) # It will return list

# Dictionary

di = {'name' : 'Corey', 'Job' : 'Programming', 'age' : None, 'OS' : 'Mac'}
s_di = sorted(di) # It will return sorted list of keys 

print("Sorted Dic", s_di)

# Key parameter with sorted function

li2  = [-6,-5,-4,1,2,3]

s_li2 = sorted(li2)
print(s_li2)

s_li2 = sorted(li2, key=abs)
print(s_li2)


# Sort Employee Object by name, age , Salary, 
class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    # str representation of class instance/object
    def __repr__(self):
        return f'{(self.name, self.age, self.salary)}'


e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]

def e_sort(emp):
    return emp.name

s_employees = sorted(employees, key=e_sort)
# s_employees = sorted(employees, key=lambda emp:emp.name)

# Amother way to do above thing is 
# from operator import attrgetter
# s_employees = sorted(employees, key=attrgetter('salary'))

print(s_employees)