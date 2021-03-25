n = int(input())
a = input().split()
res = n
for i in range(n):
    print(int(a[i]))
    if res > int(a[i]):
        res = int(a[i])

print(res)