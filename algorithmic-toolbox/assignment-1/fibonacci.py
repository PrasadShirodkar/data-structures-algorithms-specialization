# Uses python3

# Problem Description
# Task. Given an integer 𝑛,  nd the 𝑛th Fibonacci number 𝐹𝑛.
# Input Format. The input consists of a single integer 𝑛.
# Constraints. 0 ≤ 𝑛 ≤ 45.
# Output Format. Output 𝐹𝑛.
# Time Limits.
#     language          C C++ Java Python C#  Haskell JavaScript Ruby Scala
#     time in seconds   1 1    1.5   5    1.5    2        5        5    3
# Memory Limit. 512MB.

def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

n = int(input())
print(calc_fib(n))
