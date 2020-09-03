# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.
import pyperclip, re
def detect_numbers(text):
    #phone_regex = re.compile(r"(\+420)?\s*?(\d{3})\s*?(\d{3})\s*?(\d{3})")
    phone_regex = re.compile('(?:\+ *)?\d[\d\- ]{7,}\d')
    print(phone_regex.findall(text))

#(\d{3}|\(\d{3}\))?     area code
#(\s|-|\.)?             separator
#(\d{3})                first 3 digits
#(\s|-|\.)              separator
#(\d{4})                last 4 digits
#(\s*(ext|x|ext.)\s*(\d{2,5}))? extension
#)''', re.VERBOSE)



def detect_emails(text):
    #email_regex = re.compile('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
    #email_regex = re.compile('\S+@\S+')
    email_regex = re.compile('\S+@\S+.+')

    print(email_regex.findall(text))



# username [a-zA-Z0-9._%+-]+
# @ symbol
# domain name [a-zA-Z0-9.-]+
# dot-something (\.[a-zA-Z]{2,4})




detect_emails("My emails are monica@gmail.com, mo123@gmail.com, 1moni@gmail.com")
detect_numbers("My phone numbers are 123123123, (31)98324113, 3198324113, +234-123-3231 and + 555 123 1234")



#Strong Password Detection
