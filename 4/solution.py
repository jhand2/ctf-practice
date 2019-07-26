from vm import *
import re

def is_mirrored(n):
    s = []
    while n > 0:
        s.append(n % 10)
        n = n // 10

    for i in range(len(s) // 2):
        if s[i] != s[-(i+1)]:
            return False

    return True


def is_prime(n):
    """
    Assumes that n is a positive natural number

    Borrowed from: https://www.rookieslab.com/posts/fastest-way-to-check-if-a-number-is-prime-or-not
    """
    # We know 1 is not a prime number
    if n == 1:
        return False

    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i*i <= n:
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True

def decode_char(c, f):
    if c in VM.OPERATIONS:
        return VM.OPERATIONS[c].__name__
    elif ord(c) >= ord('0') and ord(c) <= ord('9'):
        for i in range(3): f.read(1)
        return str(ord(c) - ord('0'))
    else:
        return c

def replace_symbols():
    s = ''
    with open("program", "r") as f:
        while True:
            c = f.read(1)
            if not c:
                break
            s = s + decode_char(c, f)
    return s


def get_next_mirrored_prime(idx, last_prime=None, last_idx=None):
    i = 1
    prime = 2
    if last_prime is not None and last_idx is not None:
        i = last_idx
        prime = last_prime

    while i < idx:
        prime = prime + 1
        if is_mirrored(prime):
            if is_prime(prime):
                i += 1

    return prime


def main():
    # Get file and replace known symbols
    s = replace_symbols()

    with open("converted.txt", "w") as f:
        f.write(s)

    # Split instructions into sections
    s = s.split('\n\n')

    for section in s:
        # Only look at sections that are loading values onto the stack
        if section.startswith("load"):
            print(section)
            res = re.findall(r"[0-9]+", section)

            # The starting stack
            stack = res[:-1]

            print(res)
            print()

    last_prime = None
    last_idx = None
    for i in range(1, 11):
        p = get_next_mirrored_prime(i, last_prime, last_idx)
        last_prime = p
        last_idx = i
        print(p)

main()
