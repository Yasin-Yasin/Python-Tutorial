my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# index    0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# index  -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# list[start:end:step]

print(my_list[5])
print(my_list[-1]) # Last Value
print(my_list[2:7])
print(my_list[-8:-5])
print(my_list[3:-5])

print(my_list[:4]) # if we leave start value blank, it will start from zero
print(my_list[1:9]) # It will print 1 to 8 
print(my_list[1:]) # It will print 1 to 9
print(my_list[:]) # whole list

# step
print(my_list[2:-1:2])
print(my_list[-1:2:-1])
print(my_list[-1:2:-2])
print(my_list[::-1]) # Reverse List

# String Slicing

sample_url = 'http://coreyms.com'
print(sample_url)

# Reverse the url
print(sample_url[::-1])

# Get the top level domain
print(sample_url[-4:])

# Print the url without the http://
print(sample_url[7:])

# Print the url without http:// and the top level domain
print(sample_url[7:-4])