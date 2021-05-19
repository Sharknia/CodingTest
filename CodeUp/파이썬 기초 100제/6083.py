i, j, k = input().split()
for r in range(int(i)):
    for g in range(int(j)):
        for b in range(int(k)):
            print(r, g, b)
print(int(i) * int(j) * int(k))