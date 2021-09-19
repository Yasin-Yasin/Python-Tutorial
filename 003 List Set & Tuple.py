# LIST
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)
print(len(courses))

# List Slicing
print(courses[1])
print(courses[-1])
print(courses[:2])

# List Methods :
courses.append('Art')
print(courses)
courses.insert(0, 'Busuness')
print(courses)

# Insert entire list
courses2 = ['Commerce', 'English']
# courses.insert(0, courses2)
# print(courses)
# print(courses[0])

# It will extends items to list instead of a list itself
courses.extend(courses2)
print(courses)

courses.remove('English')
print(courses)

# It will remove by default last item otherwise indexed item and return the removed item
courses.pop()
print(courses)
popped = courses.pop(0)
print(popped)
print(courses)

courses.reverse()
print(courses)

# sort() method - it sort the original list
courses.sort()
print(courses)
nums = [1,5,4,3,2]
nums.sort(reverse=True)
print(nums)

# sorted () Function - It returns a new sorted list But doesn't change orignal list.
courses = ['History', 'Math', 'Physics', 'CompSci']
sorted_courses = sorted(courses)
print("Original List :",courses)
print("Sorted List :", sorted_courses)

# min() max() sum() functions
print(min(nums))
print(max(nums))
print(sum(nums))

# index method
print(courses.index('Math'))
print('Business' in courses)

# join method, Turn list into a string
course_str = ', '.join(courses)
print(course_str)
print(type(course_str))
# convert comma seperated str into a list by split method
new_list = course_str.split(', ')
print(new_list)

# for loop with function enumerate
for index, course in enumerate(courses):
    print(index, course) 

# if we want index to start from 1
for index, course in enumerate(courses, start=1):
    print(index, course)


# TUPLE - WE CANNOT MODIFY TUPLE - IMMUTABLE
print("\n\n\nTUPLE\n")

# Mutable

list_1 = ['Roti', 'Biryani', 'Chicken', 'Paratha']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Khichdi'

print(list_1)
print(list_2)

# Immutable
tuple_1 = ('Roti', 'Biryani', 'Chicken', 'Paratha')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Mutton'

# print(tuple_1)
# print(tuple_2)


# SET - Unordered list, No Duplicate
print("\n\n\nSET\n")

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses)
print('Math' in cs_courses)

# Common item of both sets
print(cs_courses.intersection(art_courses))

# different item 
print(cs_courses.difference(art_courses))

# Combine
print(cs_courses.union(art_courses))


# Create empty list, set, tuple

empty_list = []
empty_list = list()
print(empty_list)

empty_tuple = ()
empty_tuple = tuple()
print(empty_tuple)

empty_set = {} # This will create a dictionary not set
empty_set = set()
print(empty_set)






