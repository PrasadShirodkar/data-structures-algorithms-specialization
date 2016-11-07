# Uses python3
import random


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
    while True:
        # Generate random integer n between 0 and 10 to the power 7 both inclusive
        max = pow(10, 7)
        n = random.randint(0, max)
        print("Input nth Fibonacci number: " + str(n))
        fib_recurse_result = get_fibonacci_last_digit_naive(n)
        print("nth Fibonacci number's last digit by recursion: " + str(fib_recurse_result))
        fib_iter_result = get_fibonacci_last_digit_iterative(n)
        print("nth Fibonacci number's last digit by iteration: " + str(fib_iter_result))
        if fib_recurse_result != fib_iter_result:
            print("Solution failed. Please correct the solution")
            break
