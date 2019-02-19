import math

n, h = map(int, input().split())
a, b, c, d, e = map(int, input().split())

k1 = b+e
k2 = d+e
k3 = h-e*n

cost = a * n
for x in range(n+1):
    y = (-k1*x -k3) // k2 + 1
    if 0 <= y <= n-x:
        cost = min(cost, a*x+c*y)
    elif y < 0:
        cost = min(cost, a * x)
        break

print(cost)
