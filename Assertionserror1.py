#Write an assert statement that triggers an AssertionError if the variable
#spam is an integer less than 10 .

spam = 11
assert spam >= 10, 'the variable is less than 10.'


#Write an assert statement that triggers an AssertionError if the variables
#eggs and bacon contain strings that are the same as each other, even if
#their cases are different (that is, 'hello' and 'hello' are considered the
#same, and 'goodbye' and 'GOODbye' are also considered the same).

bacon = 'bacon'
eggs = 'eggs'
assert eggs != bacon, 'the variables are the same.'

bacon = 'BAcon'
eggs = 'bacon'
assert eggs.lower() != bacon.lower(), 'the variables are the same.'

#assert(False, 'This assertion always triggers.')
