def spam():
  eggs = 99
  bacon()
  print(eggs)
def bacon():
  ham = 101
  eggs = 0
spam()

#global statement
eggs = 'global'
spam()
print(eggs)
#If you ever want to modify the value stored in a global variable from in a function,
#you must use a global statement on that variable
