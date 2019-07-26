from vm import *
import re
import sys

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

def solve_section(stack, reg1, reg2, start_prime_idx):
    # Get next prime
    last_prime = None
    last_idx = start_prime_idx - 1
    while stack[-1] != 0:
        reg1 = stack.pop()
        stack.append(reg2)
        stack.append(reg1)

        p = get_next_mirrored_prime(last_idx + 1, last_prime, last_idx)
        # print(p)
        last_prime = p
        last_idx += 1
        stack.append(p)

        result = stack.pop() ^ stack.pop()
        sys.stdout.write(chr(result))
        sys.stdout.flush()

        reg2 = stack.pop() + 1

    return stack


def main():
    # Get file and replace known symbols
    s = replace_symbols()

    with open("converted.txt", "w") as f:
        f.write(s)

    # Split instructions into sections
    s = s.split('\n\n')

    stack = []
    for section in s:
        # Only look at sections that are loading values onto the stack
        if section.startswith("load"):
            res = [int(n) for n in re.findall(r"[0-9]+", section)]
            stack = stack + res[:-1]
            stack = solve_section(stack, 0, res[-1], res[-1])
    # prime_count = 0
    # i = 1
    # while prime_count < 900:
    #     if is_mirrored(i):
    #         if is_prime(i):
    #             prime_count += 1
    #             print(i, prime_count, flush=True)
    #     i += 1

main()
