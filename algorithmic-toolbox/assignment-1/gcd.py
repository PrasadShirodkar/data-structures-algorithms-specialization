# Uses python3
import sys


def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


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

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_euclidean(a, b))
