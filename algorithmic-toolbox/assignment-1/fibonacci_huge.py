# Uses python3

import sys

def get_pisano_period(n, m):

    pisano_period = [0, 1]
    while True:
        next_pisano = (pisano_period[-1] + pisano_period[-2]) % m
        next_to_next_pisano = (next_pisano + pisano_period[-1]) % m
        if next_pisano == 0 and next_to_next_pisano == 1:
            # The Pisano period always starts with 0 and 1.
            # Encountering O and 1 again indicates the start of the next Pisano period.
            break
        else:
            pisano_period.append(next_pisano)
            pisano_period.append(next_to_next_pisano)
    return pisano_period


def get_fibonacci_huge_pisano_modulo(n, m):
    if n <= 1:
        return n

    pisano_period = get_pisano_period(n, m)

    pisano_period_index = n % len(pisano_period)

    return pisano_period[pisano_period_index]


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_pisano_modulo(n, m))