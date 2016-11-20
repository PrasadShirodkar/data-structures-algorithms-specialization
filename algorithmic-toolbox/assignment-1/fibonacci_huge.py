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


def get_fibonacci_huge_iterative(n, m):
    if n <= 1:
        return n

    fibonacci = [0, 1]
    for x in range(2, n + 1):
        fibonacci.append(fibonacci[x - 1] + fibonacci[x -2])
    return fibonacci[n] % m

if __name__ == '__main__':

    while True:
        # Generate random integer n between 0 and 10 to the power 3 both inclusive
        max = pow(10, 3)
        n = random.randint(0, max)

        # Generate random integer n between 1 and 10 to the power 2 both inclusive
        max = pow(10, 2)
        m = random.randint(1, max)

        print("n = " + str(n) + " m = " + str(m))

        fibonacci_huge_naive = get_fibonacci_huge_naive(n, m)
        print("Naive result for Fibonacci " + str(n) + " modulo " + str(m) + " is " + str(fibonacci_huge_naive))

        fibonacci_huge_iterative = get_fibonacci_huge_iterative(n, m)
        print("Iterative result Fibonacci " + str(n) + " modulo " + str(m) + " is " + str(fibonacci_huge_iterative))

        if fibonacci_huge_naive != fibonacci_huge_iterative:
            print("Solution failed. Please correct the solution")
            break
