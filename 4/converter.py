from vm import *

def decode_char(c):
    if c in VM.OPERATIONS:
        return VM.OPERATIONS[c].__name__
    else:
        return c

with open("program", "r") as f:
    for c in f.read():
        print(decode_char(c), end='')
