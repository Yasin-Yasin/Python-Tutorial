# --------------------------------------- Open and reading -----------------------------------------

# f = open('test.txt', 'r') # Default is raeding - 'r'
# print(f.name)
# print(f.mode)

# f.close() # Closing the file

# Open file using context manager

with open('test.txt', 'r') as f:
    # f_content = f.read() # Read Whole file
    # print(f_content)

    # f_content1 = f.readlines() # List of eachlines
    # print(f_content1)

    # f_content2 = f.readline() # Read Single line and pointer move towards next
    # print(f_content2)

    # for line in f:
    #     print(line, end="")

    # f_content3 = f.read(100) # Read First 100 character
    # print(f_content3,end='')

    # f_content3 = f.read(100) # Read next 100 character
    # print(f_content3,end='')

    # Read Large files

    # size_to_read = 10
    # f_content4 = f.read(size_to_read)
    
    # while len(f_content4) > 0:
    #     print(f_content4, end='')
    #     f_content4 = f.read(size_to_read)

    # f.tell() and f.seek()
    size_to_read =10
    fcontent = f.read(size_to_read)
    print(fcontent, end='')

    # f.seek(0) # Set pointer to begining of the file
    f.seek(20)
    fcontent = f.read(size_to_read)
    print(fcontent)

    print(f.tell()) # Tell where the pointer is 
    

# print(f.closed) # Return True if file is closed