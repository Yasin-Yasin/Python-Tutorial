nums = [1,2,3,4,5]

# FOR LOOP

for num in nums:
    print(num)

# Break - Stop the Loop

# It will stop the loop once num == 3
for num in nums:
    if num == 3:
        print('Found')
        break
    print(num)

# Continue - It will skip the further execution and will continue to next iteration

for num in nums:
    if num == 3:
        continue
    print(num) #  Once num == 3, It will skip this line as execution will go to next iteration

# Nested Loop

for num in nums:
    for letter in 'abc':
        print(num, letter)

# range() Function

for i in range(1, 4): # Start from 1
    print(i)


# WHILE LOOP

x = 0

# while x < 5:
#     print(x)
#     x += 1


# while x < 5:
#     if x == 2:
#         break
#     print(x)
#     x += 1

while True:
    if x == 3:
        break
    print(x)
    x += 1