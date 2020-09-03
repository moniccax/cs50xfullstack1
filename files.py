import re

madlib_text = 'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'

madlib_file = open('madlib.txt', 'w')
madlib_file.write(madlib_text)

madlib_regex = re.compile(r'[A-Z]{2,}')
mo = madlib_regex.findall(madlib_text)  #acha palavras com letra maiusculas

for x in mo:
    if x == 'ADJECTIVE':
        prompt = input('Enter an adjective: ')
    else:
        prompt = input(f'Enter a {x.lower()}: ')
    madlib_text = madlib_text.replace(x, prompt, 1) #substitui com palavras encontradas em madlib_Text

print('\n' + madlib_text)

user_madlibs = open('completed_madlibs.txt', 'w')
user_madlibs.write(madlib_text)

user_madlibs.close()
madlib_file.close()
