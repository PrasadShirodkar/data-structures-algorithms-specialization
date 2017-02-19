# Uses python3
import sys


def process_change(amount, denomination):
    coins = int(amount / denomination)
    amount %= denomination
    return amount, coins


def get_change(m):
    minimum_coins = 0
    denominations = [10, 5, 1]
    while m > 0:
        for item in denominations:
            if m >= item:
                m, coins = process_change(m, item)
                minimum_coins += coins
    return minimum_coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
