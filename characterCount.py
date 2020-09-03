import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
print(count)


#The setdefault() method offers a way to ensure that a key exists. The
#first argument passed to the method is the key to check for, and the second
#argument is the value to set at that key if the key does not exist. If the key
#does exist, the setdefault() method returns the key’s value.
pprint.pprint(count)
