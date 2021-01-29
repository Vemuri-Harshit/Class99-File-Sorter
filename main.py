import shutil 
import os

# os = mkdir, os.path.exists,os.splitext
# sutil = move, copy

path = input("PATH HERE:")

list_of_files = os.listdir(path)
all_folders_with_ext = []

for  f in list_of_files:
    name , ext = os.path.splitext(f)
    ext = ext[1:]
    if ext == '': continue

    if os.path.exists(path + '/' + ext): shutil.move(path + '/' + f, path + '/' + ext + '/' + f)
    else: os.mkdir(path + '/' + ext); shutil.move(path + '/' + f, path + '/' + ext + '/' + f)