from vm import *

def decode_char(c):
    if c in VM.OPERATIONS:
        # return VM.OPERATIONS[c].__name__
        return ''
    elif ord(c) >= ord('0') and ord(c) <= ord('9'):
        return str(ord(c) - ord('0'))
    else:
        return ''
        # return c

with open("program", "r") as f:
    for c in f.read():
        print(decode_char(c), end='')
