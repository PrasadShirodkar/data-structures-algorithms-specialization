# Uses python3
import sys


def process_change(amount, denomination):
    coins = int(amount / denomination)
    amount %= denomination
    return [amount, coins]


def get_change(m):
    minimum_coins = 0
    while m > 0:
        if m >= 10:
            process_change(m, 10)
        elif m >= 5:
            process_change(m, 5)
        elif m >= 1:
            process_change(m, 1)
    return minimum_coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
