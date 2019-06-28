# Run this Python code in the folder where file names must be renamed in batch
# This code was temporarily used for changing file names of a project.
# Be careful to customize to new applications.

import glob, re, os

def mass_rename(file_ext):
   path_list = glob.glob('*.' + file_ext)
   pattern = r'(.+-t)(\d+)(\..+)'
   # first rename to temporary base name
   # if temporary naming system is not used, then the renamed file may overwrite another old file
   for name in path_list:
     name_parts = re.search(pattern, name).groups()
     page_no = int(name_parts[1])
     new_page = page_no + 10
     new_name = name_parts[0] + str(new_page) + name_parts[2]
     os.system("mv " + name + " temp_" + new_name)
   path_list2 = glob.glob('*.' + file_ext)
   pattern = r'temp_KFZ_(.+)'
   for name in path_list2:
     name_parts = re.search(pattern, name).groups()
     new_name = name_parts[0]
     os.system("mv " + name + " Oto_" + new_name)

#mass_rename('docx')
mass_rename('pdf')


def mass_rename_aligned_files(file_ext):
   path_list = glob.glob('*.' + file_ext)
   pattern = r'(.+-t)(\d+)(.+-t)(\d+)(\..+)'
   # first rename to temporary base name
   # if temporary naming system is not used, then the renamed file may overwrite another old file
   for name in path_list:
     name_parts = re.search(pattern, name).groups()
     page_no = int(name_parts[1])
     new_page = page_no + 10
     new_name = name_parts[0] + str(new_page) + name_parts[2] + str(new_page) + name_parts[4]
     os.system("mv " + name + " temp_" + new_name)
   path_list2 = glob.glob('*.' + file_ext)
   pattern = r'temp_(.+)'
   for name in path_list2:
     name_parts = re.search(pattern, name).groups()
     new_name = name_parts[0]
     os.system("mv " + name + " " + new_name)

#mass_rename_aligned_files('csv')
#mass_rename_aligned_files('tmx')
mass_rename_aligned_files('xls')
