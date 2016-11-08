# Uses python3
import sys


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def lcm_efficient(a, b):
    product = a * b
    gcd = gcd_euclidean(a, b)
    return product // gcd


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


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_efficient(a, b))