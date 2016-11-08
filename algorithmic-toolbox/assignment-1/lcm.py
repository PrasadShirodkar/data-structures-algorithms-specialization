# Uses python3
import random


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def lcm_efficient(a, b):
    product = a * b
    gcd = gcd_euclidean(a, b)
    lcm = int(product / gcd)
    return lcm


def gcd_euclidean(a, b):
    if a < b:
        d = b % a
        dividend = a
    else:
        d = a % b
        dividend = b
    if d == 0:
        return dividend
    else:
        return gcd_euclidean(dividend, d)


while True:
    # Generate random integer n between 1 and 10 to the power 9 both inclusive
    max = pow(10, 9)
    a = random.randint(1, max)
    b = random.randint(1, max)
    print(a, b)
    lcm_eff = lcm_efficient(a, b)
    print("lcm_efficient: " + str(lcm_eff))
    lcm_slow = lcm_naive(a, b)
    print("lcm naive: " + str(lcm_slow))
    if lcm_eff != lcm_slow:
        print("Solution failed. Please correct the solution")
        break
