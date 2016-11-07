# Uses python3
import random

# Problem Description
# Task. Given an integer 𝑛, find the 𝑛th Fibonacci number 𝐹𝑛.
# Input Format. The input consists of a single integer 𝑛.
# Constraints. 0 ≤ 𝑛 ≤ 45.
# Output Format. Output 𝐹𝑛.
# Time Limits.
#   ------------------------------------------------------------------------
#     language          C C++ Java Python  C#  Haskell JavaScript Ruby Scala
#   ------------------------------------------------------------------------
#     time in seconds   1 1    1.5   5     1.5    2        5        5    3
#   ------------------------------------------------------------------------
# Memory Limit. 512MB.

def calc_fib(n):
    if n <= 1:
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib_iter(n):
    if n <= 1:
        return n

    fib = [0, 1]
    for x in range(2, n + 1):
        fib.append(fib[x - 1] + fib[x -2])
    return fib[n]

if __name__ == '__main__':
    while True:
        # Generate random integer n between 0 and 45 both inclusive
        n = random.randint(0, 45)
        print("Input nth Fibonacci number: " + str(n))
        fib_recurse_result = calc_fib(n)
        print("nth Fibonacci number result by recursion: " + str(fib_recurse_result))
        fib_iter_result = calc_fib_iter(n)
        print("nth Fibonacci number result by iteration: " + str(fib_iter_result))
        if fib_recurse_result != fib_iter_result:
            print("Solution failed. Please correct the solution")
            break
