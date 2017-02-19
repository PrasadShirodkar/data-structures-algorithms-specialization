# Uses python3
import sys

def sort_weights_values(weights, values):
    # Sort weights and values in non-increasing order computed from value per unit weight
    value_per_weight = list()
    n = len(values)
    for i in range(n):
        value_per_weight.append(values[i] / weights[i])

    zipped = zip(value_per_weight, values, weights)
    sorted_zipped = sorted(zipped, reverse = True)
    value_per_weight, values, weights = zip(*sorted_zipped)
    return values, weights


def get_optimal_value(capacity, weights, values):
    value = 0.
    values, weights = sort_weights_values(weights, values)
    for i, weight in enumerate(weights):
        if capacity <= 0:
            return value
        min_weight = min(capacity, weight)
        value += min_weight * values[i] / weights[i]
        capacity -= min_weight

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
