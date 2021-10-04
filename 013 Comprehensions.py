# ---------------------------- LIST COMPREHENSIONS --------------------------------------

nums = [1,2,3,4,5,6,7,8,9,10]

#            *** I want 'n' for each 'n' in nums : ***

my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

# By List Comprehension
my_comp_list = [n for n in nums] 
print(my_comp_list)


#           *** 'n*n' for each 'n' in nums : ***

my_list1 = []
for n in nums:
    my_list1.append(n*n)
print(my_list1)

# By List Comprehension
my_comp_list1 = [n*n for n in nums]
print('comp', my_comp_list1)

# Using a map + lambda
my_list2 = map(lambda n: n*n, nums)
print('map', list(my_list2)) # As map function return map object so we can call list constructer to turn it into list

#           *** I want 'n' for each 'n' in nums if 'n' is even : ***

my_list3 = []
for n in nums:
    if n%2 == 0:
        my_list3.append(n)
print(my_list3)

# By List Comprehension
my_comp_list3 = [n for n in nums if n%2 == 0]
print('comp', my_comp_list3)

# Using Filter + lambda(
my_filter_list3 = filter(lambda n: n%2 == 0, nums)
print('filter', list(my_filter_list3))

# *         *** I want a (letter, num) pair for each letter in 'abcd' and each number in '0123' ***

my_list4 = []
for letter in 'abcd':
    for num in range(4):
        my_list4.append((letter, num))

print(my_list4)

# By List Comprehension
my_list4 = [(letter, num) for letter in 'abcd' for num in range(4)] 
print("Comp.", my_list4)

# ------------------------------ Dictionary Comrehension ----------------------------------

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
print(list(zip(names, heroes))) # List of tuple which will contain matching index of both lists

#           *** dic{name:hero} ***

my_dic ={}
for name, hero in zip(names, heroes):
    my_dic[name] = hero
print(my_dic)

# By dictionary Comprehension
my_comp_dic = {name: hero  for name,hero in zip(names, heroes)}   
print('comp', my_comp_dic)

# if name not equal to peter
my_comp_dic = {name: hero  for name,hero in zip(names, heroes) if name!= 'Peter'}   
print(my_comp_dic)


# ----------------------------------- Set Comprehension ---------------------------------------

numss = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
my_set = set()
for n in numss:
    my_set.add(n)
print(my_set)

# By Set Comprehension
my_comp_set = {n for n in numss}
print(my_comp_set)

# ----------------------------------- Generator Expressions ------------------------------------

#              *** yield n*n for each n in numss ***

nums1 = [1,2,4,5,6,7,8,9,10]

def gen_func(nums):
    for n in nums:
        yield n*n

my_gen = gen_func(nums1)

for i in my_gen:
    print (i)

# Comprehension
my_comp_gen = (n*n for n in nums)

for i in my_comp_gen:
    print(i)