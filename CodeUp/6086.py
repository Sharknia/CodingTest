sum = int(input())
result = 0
for i in range(1, sum+1):
    result += i
    if result >= sum:
        print(result)
        break