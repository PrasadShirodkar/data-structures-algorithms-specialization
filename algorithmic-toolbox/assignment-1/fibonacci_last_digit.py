# Uses python3
import sys


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def get_fibonacci_last_digit_iterative(n):
    if n <= 1:
        return n

    fibonacci_last_digit = [0, 1]

    for x in range(2, n + 1):
        fibonacci_last_digit.append((fibonacci_last_digit[x - 1] + fibonacci_last_digit[x - 2]) % 10)

    return fibonacci_last_digit[n]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_iterative(n))
