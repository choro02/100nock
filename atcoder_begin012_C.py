n = int(input())

N = 2025

r = N - n

a = [i for i in range(1,10) if r % i == 0 and r // i < 10]
b = ['{x} x {y}'.format(x=i, y=r//i) for i in a]

for i in b:
    print(i)