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


for i in range(1000):
    if is_mirrored(i) and is_prime(i):
        print(i)

