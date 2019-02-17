n = int(input())
ng1 = int(input())
ng2 = int(input())
ng3 = int(input())

ans = 'NO'

print(n,ng1,ng2,ng3)

count = 1

while n >= 0:

    if n == ng1 \
        or n  == ng2 \
        or n  == ng3:
        break

    if n > 3:
        if count < 100:
            count += 1
        else:
            print('Count Over')
            break

        if n - 3 != ng1 \
            and n - 3 != ng2 \
            and n - 3 != ng3:
            n -= 3

        elif n - 2 != ng1 \
            and n - 2 != ng2 \
            and n - 2 != ng3:
            n -= 2

        elif n - 1 != ng1 \
            and n - 1 != ng2 \
            and n - 1 != ng3:
            n -= 1 

        else:
            break

    if 0 < n <= 3:
        n -= n

    if n == 0:
        ans = 'YES'
        break

    print(n, count)



print(ans)