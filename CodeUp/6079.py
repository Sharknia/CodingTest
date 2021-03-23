a = int(input())
i=1
result = 0
while True:
    result += i
    if result >= a:
        print(i)
        break
    i += 1