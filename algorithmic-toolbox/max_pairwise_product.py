# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0

x = 0
y = 0
for i in range(0, n):
    if a[i] <= x and a[i] <= y:
        pass
    else:
        if x > y:
            y = a[i]
        else:
            x = a[i]
result = x * y

print(result)
