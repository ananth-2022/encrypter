import string
import time
import random

chars = string.ascii_letters+string.digits+string.punctuation

def constructmap(seed):
    conversion = list(chars)
    random.seed(seed)
    random.shuffle(conversion)
    map = dict(zip(chars, conversion))
    return map

t = int(time.time())
m = constructmap(t)
#print(m)

def encrypt(string, map):
    temp = ""
    for char in string:
        if char in chars:
            temp += map[char]
        else:
            temp += char
    temp = list(temp)
    random.shuffle(temp)
    ret = ""
    for c in temp:
        ret += c
    return ret

choice = input('encrypt or compare? E/C')
if choice == 'e':
    text = input("what to encrypt?")
    print(encrypt(text, m))
    print('key = ', t)
else:
    text = input("what to compare?")
    htext = input('hash?')
    key = int(input('key?'))
    map = constructmap(key)
    if encrypt(text, map) == htext:
        print('yes')
    else:
        print('no')