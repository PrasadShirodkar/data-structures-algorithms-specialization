# Uses python3
import random

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

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


def get_fibonacci_huge_modulo_pisano(n, m):

    if n not in range(1, pow(10, 18) + 1):
        raise ValueError("Value of n is not in the valid range from 1 to 10^18.")

    if m not in range(2, pow(10, 5) + 1):
        raise ValueError("Value of m is not in the valid range from 1 to 10^5.")

    pisano_period = get_pisano_period(n, m)

    pisano_period_index = n % len(pisano_period)

    return pisano_period[pisano_period_index]


if __name__ == '__main__':

    while True:
        # Generate random integer n between 1 and 10 to the power 3 both inclusive
        max = pow(10, 3)
        n = random.randint(1, max)

        # Generate random integer n between 2 and 10 to the power 2 both inclusive
        max = pow(10, 2)
        m = random.randint(2, max)

        print("n = " + str(n) + " m = " + str(m))

        fibonacci_huge_naive = get_fibonacci_huge_naive(n, m)
        print("Naive result for Fibonacci " + str(n) + " modulo " + str(m) + " is " + str(fibonacci_huge_naive))

        fibonacci_huge_modulo_pisano = get_fibonacci_huge_modulo_pisano(n, m)
        print("Pisano result Fibonacci " + str(n) + " modulo " + str(m) + " is " + str(fibonacci_huge_modulo_pisano))

        if fibonacci_huge_naive != fibonacci_huge_modulo_pisano:
            print("Solution failed. Please correct the solution")
            break
