# Uses python3
import random

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def get_pisano_period(m):

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


def fibonacci_sum_last_digit(n):

    # To find the repeating sequence of last digits of Fibonacci numbers, find the Pisano period using 10
    pisano_period = get_pisano_period(10)

    remainder = (n + 2) % len(pisano_period)

    last_digit = pisano_period[remainder]



    return last_digit - 1


if __name__ == '__main__':

    while True:
        # Generate random integer n between 1 and 10 to the power 3 both inclusive
        max = pow(10, 3)
        n = random.randint(1, max)

        print("n = " + str(n))

        fibonacci_sum_naive_result = fibonacci_sum_naive(n)
        print("Last digit for sum of Fibonacci " + str(n) + " is " + str(fibonacci_sum_naive_result))

        fibonacci_sum_last_digit_result = fibonacci_sum_last_digit(n)
        print("Last digit for sum of Fibonacci " + str(n) + " is " + str(fibonacci_sum_last_digit_result))

        if fibonacci_sum_naive_result != fibonacci_sum_last_digit_result:
            print("Solution failed. Please correct the solution")
            break