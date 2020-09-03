#Deleting Unneeded Files
#It’s not uncommon for a few unneeded but humongous files or folders to
#take up the bulk of the space on your hard drive. If you’re trying to free up
#Organizing Files     213room on your computer, you’ll get the most bang for your buck by deleting
#the most massive of the unwanted files. But first you have to find them.
#Write a program that walks through a folder tree and searches for excep-
#tionally large files or folders—say, ones that have a file size of more than
#100MB. (Remember, to get a file’s size, you can use os.path.getsize() from
#the os module.) Print these files with their absolute path to the screen.
import shutil #shell utilities
import os
import re
from send2trash import send2trash
## REVIEW: re

#Calling os.unlink(path) will delete the file at path .
#Calling os.rmdir(path) will delete the folder at path . This folder must be
#empty of any files or folders.
#Calling shutil.rmtree(path) will remove the folder at path , and all files
#and folders it contains will also be deleted.

#Using send2trash is much safer than Python’s regular delete functions,
#send2trash.send2trash('bacon.txt')


# folder where .py is
path = os.getcwd()
# for storing the size of
# the largest file
max_size = 0

# for storing the path to the
# largest file
max_file =""

# walking through the entire folder,
# including subdirectories

for folder, subfolders, files in os.walk(path):

    # checking the size of each file
    for file in files:
        size = os.stat(os.path.join( folder, file  )).st_size

        # updating maximum size
        if size>max_size:
            max_size = size
            max_file = os.path.join( folder, file  )

print("The largest file was: "+max_file)
print('Size: '+str(max_size)+' bytes')
if max_size>618562:
    send2trash(max_file)
