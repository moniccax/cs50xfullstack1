#Calling os.path.abspath(path) will return a string of the absolute path
#of the argument. This is an easy way to convert a relative path into an
#absolute one.
#Calling os.path.isabs(path) will return True if the argument is an abso-
#lute path and False if it is a relative path.
#Calling os.path.relpath(path, start) will return a string of a relative path
#from the start path to path . If start is not provided, the current working
#directory is used as the start path.


#Call the open() function to return a File object.
# open('.txt', a) acrescenta no final do arquivo. open('.txt', w) reescreve no arquivo. -r escreve no arquivo.


#Call the read() or write() method on the File object.

#read() method returns the file’s entire contents as a single string
#value. The readlines() method returns a list of strings, where each
#string is a line from the file’s contents.

#Close the file by calling the close() method on the File object.


#os.getcwd() function returns the current working directory. The os.chdir() function changes the current working directory.


#A shelf value resembles a dictionary value; it has keys and values, along
#with keys() and values() methods that work similarly to the dictionary
#methods of the same names.


import os
import re
namefile = open('text.txt')
str = namefile.read()
# https://stackoverflow.com/questions/37666790/how-to-join-chapter-8-automate-the-boring-stuff
#print('Enter an adjective')
#adjective = input()
adjective = 'nice'
adj='ADJECTIVE'

str.replace(adj, adjective,1)
print(str)
if (str.find('ADJECTIVE') != -1):
    str.replace("ADJECTIVE", adjective, 1)
else:
    print ("Doesn't contains adjective")
print('Enter a noun')
noun = input()
if (str.find('NOUN') != -1):
    str.replace("NOUN", noun)
else:
    print ("Doesn't contains noun")
print('Enter a verb')
verb = input()
if (str.find('VERB') != -1):
    str.replace("VERB", verb)
else:
    print ("Doesn't contains verb")

print (str)
