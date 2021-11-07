import os

os.chdir('019 Rename Filenames') # Change directory to one where files are 

# print(os.getcwd())

# Split Extention
for file in os.listdir():
    # os.path.splitext returns tuple - (file_name, file_ext)
    file_name, file_ext = os.path.splitext(file)
    # file_name.split return a list [f_title, f_course, f_num]
    f_title, f_course, f_num = file_name.split('-') 

    # Remove White Spaces
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2)  # 1 to end, zfill(2) - add zero before number and make it 2 digit

    new_name = '{}-{}{}'.format(f_num, f_title, file_ext)

    os.rename(file, new_name)



