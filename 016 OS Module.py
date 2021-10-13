import os
from datetime import datetime # To convert timestamp to human readable format

# To see methods and functions available in Module
# print(dir(os)) 

# Get current working directory
print(os.getcwd())

# Change Directory
os.chdir('/home/Yasin/Desktop')
print(os.getcwd())

# View files and directory 
print(os.listdir())

# Create a folder
# os.mkdir('Demo_OS') 

# If parent directory/directories doesn't exist then use makedirs as it will create that directories as well
# os.makedirs('Test/Sub_Dir')

# Remove dir 
# os.rmdir('Demo_OS')

# It will remove parent directories as well - Use carefully
# os.removedirs('Test/Sub_Dir')

# Rename File or Directory
# os.rename('test.txt', 'demo.txt')

# Information about file
print(os.stat('demo.txt').st_size) # Size of a file
mod_time = os.stat('demo.txt').st_mtime # Last modification time 
print(datetime.fromtimestamp(mod_time)) # Convert timestamp to regular format

# Entire Directory Tree
# for dirpath, dirnames, filenames in os.walk('/home/Yasin/Desktop'):
#     print('Current Path: ', dirpath)
#     print('Directories: ', dirnames)
#     print('Files: ', filenames)
#     print() # for newline


# Environmenr variable - $Home

# print(os.environ.get('HOME'))

# ----------------------------------- os.path ----------------------------------

# Combine Path
filepath = os.path.join(os.environ.get('HOME'), 'test.txt')
print(filepath)

# with open (filepath, 'w') as f:
#     f.write('This is test file')


# Filename from path
print(os.path.basename('/tmp/test.txt'))

# Dirname from path
print(os.path.dirname('/tmp/test.txt'))

# Both of them
print(os.path.split('/tmp/test.txt'))

# Check if path exist
print(os.path.exists('/tmp/test.text'))

# check if it is dir or file
print(os.path.isdir('/home/Yasin/Desktop/Python'))
print(os.path.isfile('/home/Yasin/Desktop/demo.txt'))

# Split extension from file
print(os.path.splitext('/home/Yasin/Desktop/demo.txt'))

# print(dir(os.path))