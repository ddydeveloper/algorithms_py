import math


def is_prime(value):
    if value <= 1:
        return False

    if value <= 3:
        return True

    if value % 2 == 0 or value % 3 == 0:
        return False

    sq_rt = math.sqrt(value)
    iter_until = int(sq_rt + 1)

    for i in range(5, iter_until, 6):
        if value % i == 0 or value % (i + 2) == 0:
            return False

    return True


def next_prime(value):
    if value <= 1:
        return 2

    prime = value
    found = False

    while not found:
        prime = prime + 1

        if is_prime(prime):
            found = True

    return prime


primes = []
primes_al = []

for i in range(990, 1000):
    if is_prime(i):
        primes.append(i)

print(primes)
