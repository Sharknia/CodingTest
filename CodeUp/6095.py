n = int(input())
d = [[0 for j in range(20)] for i in range(20)] 
for i in range(n):
    x,y = map(int, input().split())
    d[x-1][y-1] = 1

for i in range(19) : 
    for j in range(19) :  
        print(d[i][j], end=' ')
    print()